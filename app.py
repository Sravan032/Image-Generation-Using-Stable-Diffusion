from diffusers import StableDiffusionPipeline
import torch
import gradio as gr

# Load Stable Diffusion Model
model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

# Define Image Generation Function
def generate_image(prompt):
    image = pipe(prompt).images[0]
    return image

# Launch Gradio Interface
gr.Interface(
    fn=generate_image,
    inputs=gr.Textbox(lines=1, placeholder="Enter your prompt here..."),
    outputs="image",
    title="Stable Diffusion Image Generator",
    description="Enter a text prompt to generate an image using Stable Diffusion v1.5"
).launch()
