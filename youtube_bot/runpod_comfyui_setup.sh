#!/bin/bash
# runpod_comfyui_setup.sh
# 
# Run this script on a fresh RunPod ComfyUI pod to completely set up 
# the LTXV-13B pipeline environment.

set -e

# Define base paths
COMFY_DIR="/workspace/runpod-slim/ComfyUI"
MODELS_DIR="$COMFY_DIR/models"

echo "=========================================="
echo "🚀 Starting LTXV-13B RunPod Setup..."
echo "=========================================="

# 1. Update ComfyUI to support the latest models and features
echo "--> Updating ComfyUI core..."
cd $COMFY_DIR
git pull

# 2. Install necessary pip packages
echo "--> Installing huggingface_hub..."
pip install -q huggingface_hub

# 3. Create required model directories
echo "--> Creating directories..."
mkdir -p $MODELS_DIR/checkpoints
mkdir -p $MODELS_DIR/loras
mkdir -p $MODELS_DIR/text_encoders
mkdir -p $MODELS_DIR/latent_upscale_models

# 4. Download Checkpoint (LTXV-13B FP8)
echo "--> Downloading LTXV-13B FP8 Checkpoint (~15GB)..."
hf download Lightricks/LTX-Video \
  ltxv-13b-0.9.8-dev-fp8.safetensors \
  --local-dir $MODELS_DIR/checkpoints/

# 5. Download Text Encoder (T5-XXL FP8)
echo "--> Downloading T5-XXL FP8 Text Encoder (~5GB)..."
hf download comfyanonymous/flux_text_encoders \
  t5xxl_fp8_e4m3fn.safetensors \
  --local-dir $MODELS_DIR/text_encoders/

# 6. Download Latent Upscaler
echo "--> Downloading Spatial Upscaler..."
hf download Lightricks/LTX-Video \
  ltxv-spatial-upscaler-0.9.8.safetensors \
  --local-dir $MODELS_DIR/latent_upscale_models/

# 7. Download Distilled LoRA
echo "--> Downloading Distilled LoRA..."
hf download Lightricks/LTX-Video \
  ltxv-13b-0.9.7-distilled-lora128.safetensors \
  --local-dir $MODELS_DIR/loras/

echo "=========================================="
echo "✅ Setup Complete!"
echo "=========================================="
echo "Please restart your ComfyUI server/pod for the git pull to take effect."
