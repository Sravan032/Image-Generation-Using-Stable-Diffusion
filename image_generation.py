
from diffusers import StableDiffusionPipeline
import torch
import time

MODEL_ID = "runwayml/stable-diffusion-v1-5"

pipe = StableDiffusionPipeline.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float16
)

pipe = pipe.to("cuda")


def generate_image(prompt, steps=30, guidance_scale=7.5):

    start_time = time.time()

    result = pipe(
        prompt=prompt,
        num_inference_steps=steps,
        guidance_scale=guidance_scale
    )

    image = result.images[0]

    generation_time = time.time() - start_time

    return image, generation_time
