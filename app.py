import gradio as gr
from generate_recipe import generate_recipe
from load_model import load_model


def create_gradio_interface(model_path):

    def generate_recipe_wrapper(image, user_goals):
        return generate_recipe(image, user_goals, model, processor)

    # Load the model and processor from the model path to create the application
    processor, model = load_model(model_path)

    # Gradio interface
    image_input = gr.Image(
        type="pil", label="What Ingredients Will You Be Using?", width=400, height=600
    )
    goals_input = gr.Textbox(lines=4, label="What are your Fitness & Nutrition Goals?")
    recipe_output = gr.Textbox(label="What You Can Do With These Ingredients", lines=20)
    interface = gr.Interface(
        fn=generate_recipe_wrapper,
        inputs=[image_input, goals_input],
        outputs=recipe_output,
        title="NutriLLaVA",
        allow_flagging="never",
    )

    return interface


if __name__ == "__main__":
    interface = create_gradio_interface("llava-hf/llava-v1.6-34b-hf")
    interface.queue().launch(share=True)
