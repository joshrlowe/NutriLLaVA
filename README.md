# NutriLLaVA

NutriLLaVA is a multimodal application that generates personalized recipe suggestions given images of ingredients that a user possesses and the user's dietary goals.

## How To Run This Application

To run this application, you can clone the associated [Google Colaboratory](https://colab.research.google.com/drive/1ZBZb_qAjpyMku84J0mOy-apOTZt7lJAn?usp=sharing) into your own Google drive. Make sure you are at least using some type of GPU, preferably a NVIDIA A100. To do this, go to Runtime -> Change Runtime Type -> NVIDIA A100 and High RAM toggled On. Once the proper environment is configured, click on Runtime -> Run All. After a few minutes, a link to a Gradio interface should appear. That is your NutriLLaVA application running in Colab.

To this project on your local machine, follow these steps:

1. Clone the repository.

```bash
git clone https://github.com/yourusername/NutriLLaVA.git
```

2. Go into the NutriLLaVA directory.

```bash
cd NutriLLaVA
```

3. Create a virtual envrionment, activate it, and install all dependencies.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

4. Run the main script in `app.py`:

```bash
python3 app.py
```

## Using the Images & Conducting Tests

In the `images` directory, I have the images that were synthetically generated using ChatGPT 5.1 to have the most robust dataset.

To reproduce tests, run the app as explained in the section above, then for each image, run the application using the following 4 user profiles:

- "I am trying to gain muscle while not putting on any body fat. I want a high-protein, moderate-carb diet to support this process."
- "I am trying to lose body fat while maintaining as much muscle as possible. I want a high-protein, low-carb diet to support this process, while only consuming healthy fats."
- "I am vegan, and want my diet to be strictly plant-based."
- "I don't have any fitness goals right now, and just want to come up with some ideas on what I can make with what's in my refridgerator."

In total, there should be 80 tests to run on LLaVA 1.6 with 34 billion parameters.

## References

This project utilizes the LLaVA foundation model introduced in [Visual Instruction Tuning](https://arxiv.org/pdf/2304.08485) by Liu et. al.

To set up this project, I learned a lot from tutorials from the Hugging Face documentation on these models, particularly at the following links:

- [https://huggingface.co/llava-hf/llava-v1.6-34b-hf](https://huggingface.co/llava-hf/llava-v1.6-34b-hf)
- [https://huggingface.co/llava-hf/llava-1.5-7b-hf](https://huggingface.co/llava-hf/llava-1.5-7b-hf)

These helped me learn how to load LLaVA 1.5 and LLaVA 1.6 in development.

Additionally, I used the gradio documentation to learn how to quickly create effective gradio interfaces:

- [https://www.gradio.app/docs](https://www.gradio.app/docs)

## Extra Notes

- This model was downloaded from HuggingFace and an application was built on top of it, so this is a type C project. In the rubric, there is a section for pretrained models, and I just wanted to note that this is not applicable here.
- This code repository was formatted using [`black`](https://black.readthedocs.io/en/stable/) and prettier.
