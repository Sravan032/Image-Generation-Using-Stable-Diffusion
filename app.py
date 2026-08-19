
import gradio as gr
from image_generation import generate_image


def generate(prompt, steps, guidance_scale):

    if not prompt or not prompt.strip():
        return None, "Please enter a prompt."

    try:

        image, generation_time = generate_image(
            prompt=prompt,
            steps=int(steps),
            guidance_scale=float(guidance_scale)
        )

        result_text = f"Generation time: {generation_time:.2f} seconds"

        return image, result_text

    except Exception as e:

        return None, f"Error: {str(e)}"


with gr.Blocks(title="AI Image Generator") as demo:

    gr.Markdown(
        """
        # AI Image Generator
        ### Generate images from natural language prompts using Stable Diffusion
        """
    )

    with gr.Row():

        with gr.Column():

            prompt = gr.Textbox(
                label="Prompt",
                placeholder="Describe the image you want to generate...",
                lines=4
            )

            steps = gr.Slider(
                minimum=10,
                maximum=50,
                value=30,
                step=1,
                label="Inference Steps"
            )

            guidance_scale = gr.Slider(
                minimum=1,
                maximum=15,
                value=7.5,
                step=0.5,
                label="Guidance Scale"
            )

            generate_button = gr.Button("Generate Image")

        with gr.Column():

            output_image = gr.Image(
                label="Generated Image",
                type="pil"
            )

            generation_info = gr.Textbox(
                label="Generation Information",
                interactive=False
            )

    generate_button.click(
        fn=generate,
        inputs=[
            prompt,
            steps,
            guidance_scale
        ],
        outputs=[
            output_image,
            generation_info
        ]
    )


if __name__ == "__main__":
    demo.launch(share=True)
