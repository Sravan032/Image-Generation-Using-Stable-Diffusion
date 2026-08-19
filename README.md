# Stable Diffusion Image Generation

## Project Overview

This project demonstrates an interactive **text-to-image generation application** built using **Stable Diffusion, Hugging Face Diffusers, Python, PyTorch, and Gradio**.

The application runs on **Google Colab with GPU acceleration** and allows users to generate AI-generated images from natural language prompts through an interactive web interface.

The project also evaluates Stable Diffusion inference performance by measuring image generation time and experimenting with different inference-step configurations.

## Features

- Generate images from natural language text prompts
- Stable Diffusion v1.5 image generation
- GPU-accelerated inference using CUDA
- Interactive Gradio web interface
- Configurable inference steps
- Configurable guidance scale
- Displays image generation time
- Performance evaluation across multiple prompts
- Comparison of inference configurations for generation-time optimization
- Google Colab-based execution

## Technology Stack

- **Programming Language:** Python
- **Generative AI:** Stable Diffusion v1.5
- **ML Framework:** PyTorch
- **Model Library:** Hugging Face Diffusers
- **Interface:** Gradio
- **Execution Environment:** Google Colab
- **Hardware Acceleration:** CUDA GPU

## Project Workflow

```text
User Prompt
     |
     v
Gradio Web Interface
     |
     v
Stable Diffusion Pipeline
     |
     v
GPU-Accelerated Inference
     |
     v
Generated Image
     |
     v
Generation Time
