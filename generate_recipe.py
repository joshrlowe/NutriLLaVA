import torch
from PIL import Image
from load_model import load_model
from prompts import ingredient_identification_prompt, recipe_generation_prompt


def generate_recipe(image: Image.Image, user_goals: str, model, processor):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Set up the conversation, which will start with the ingredient identification prompt from prompts.py
    conversation = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": ingredient_identification_prompt},
                {"type": "image"},
            ],
        },
    ]

    prompt_ingredients = processor.apply_chat_template(
        conversation, add_generation_prompt=True
    )

    inputs = processor(
        text=prompt_ingredients, images=image, return_tensors="pt"
    ).to(device, model.dtype)
    output = model.generate(**inputs, max_new_tokens=100)

    # Extract the ingredients from the model's response
    ingredients_response = processor.decode(output[0], skip_special_tokens=False)
    identified_ingredients = ingredients_response.split("<|im_start|> assistant")[-1].split("<|im_end|>")[0].strip()

    # Add the identified ingredients to the conversation and build the recipe generation prompt
    conversation.append({"role": "assistant", "content": identified_ingredients})
    recipe_prompt = recipe_generation_prompt.format(ingredients=identified_ingredients, user_goals=user_goals)
    conversation.append({"role": "user", "content": [{"type": "text", "text": recipe_prompt}]})

    final_prompt = processor.apply_chat_template(conversation, add_generation_prompt=True)
    inputs_final = processor(text=final_prompt, images=image, return_tensors="pt").to(device, model.dtype)

    # Generate the final recipe suggestion and extract the recipe text
    final_output = model.generate(**inputs_final, max_new_tokens=100, do_sample=True)
    final_response_full = processor.decode(final_output[0], skip_special_tokens=False)
    recipe_text = final_response_full.split("<|im_start|> assistant")[-1].split("<|im_end|>")[0].strip()

    return recipe_text
