# Stable Diffusion Image Generation

** Project Overview**  

This project demonstrates how to generate images using Stable Diffusion on Google Colab. It allows users to input prompts and generate high-quality AI-generated images. The project also includes an interactive Gradio UI for easy image generation.  

## Features  

- Generate images using text prompts  
- Customize inference settings (guidance scale, steps, seed)  
- Batch image generation (multiple images per prompt)  
- Interactive Gradio Web UI for real-time image generation  
- Easy deployment using Google Colab  

## Setup Instructions  

### Install Dependencies  

Run the following command in Google Colab or your local system:  

```bash
pip install diffusers transformers accelerate safetensors gradio
```

Run Stable Diffusion Model
Use the provided Colab notebook or execute the Python script:
```bash
python scripts/generate_images.py
```
Launch Interactive Web UI (Gradio)
To run the Gradio UI for user-friendly image generation:
```bash
python scripts/gradio_app.py
```
[Open in Google Colab](https://colab.research.google.com/drive/1sXd7hhxdgo7xLkuXJNxBcTA0CMnrds4d?usp=sharing)
