import gradio as gr
from image_generation import generate_image

# Launch Gradio Interface
gr.Interface(
    fn=generate_image,
    inputs=gr.Textbox(lines=1, placeholder="Enter your prompt here..."),
    outputs="image",
    title="Stable Diffusion Image Generator",
    description="Enter a text prompt to generate an image using Stable Diffusion v1.5"
).launch()
