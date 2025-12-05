import torch
from transformers import LlavaNextForConditionalGeneration, LlavaNextProcessor


def load_model(model_path):
    processor = LlavaNextProcessor.from_pretrained(model_path)

    # If a GPU is available, load the mode on the GPU
    if torch.cuda.is_available():
        model = LlavaNextForConditionalGeneration.from_pretrained(
            model_path,
            torch_dtype=torch.float16,
            low_cpu_mem_usage=True,
            device_map="cuda"
        )
        
    # If no GPU is available, then load the model on the CPU - this will be so much slower
    else:
        model = LlavaNextForConditionalGeneration.from_pretrained(
            model_path,
            torch_dtype=torch.float16,
            low_cpu_mem_usage=True
        )
        model.to("cpu")
    
    return processor, model