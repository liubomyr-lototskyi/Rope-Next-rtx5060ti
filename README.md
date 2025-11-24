
<h3>I've been seeing a fast-growing wave of people rushing to buy RTX 5090, 5080, 5070, and other Blackwell cards (RTX 50-series), only to discover that their usual tools instantly break because of CUDA incompatibility.

This applies to this Rope setup, stable-diffusion-webui, fooocus, and a number of other popular programmes. What to do in this situation? Install CUDA 12.8, install library versions that support it, such as torch nightly, and compile packages yourself if they do not yet have native support for the Broadwell generation (RTX 50xx).</h3>

Most of these projects are still built for CUDA 12.1–12.4 and PyTorch 2.3/2.4 stable. The new RTX 50-series cards (Blackwell architecture) require CUDA 12.8+, and the current stable PyTorch releases simply don’t support it yet.

After spending more than 20 hours testing different versions of CUDA, torch, torchvision, and various versions of wheels, I finally found a working setup.

<h1>Important: it works for me on RTX 5060TI 16GB, but I cannot guarantee that it will work on other 50x versions of NVIDIA.</h1>

Working combination:
Python: 3.12.10

ONNXRuntime GPU: onnxruntime-gpu==1.22.0 (whl: onnxruntime_gpu-1.22.0-cp312-cp312-win_amd64.whl)

CUDA: 12.2

cuDNN: 8.9.x (also dll-s should be send at C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.2\bin)

PATH written at bin and libnvvp CUDA

pip install torch==2.7.1+cu128 torchvision==0.22.1+cu128 torchaudio==2.7.1 --index-url https://download.pytorch.org/whl/cu128

If you daily-drive local AI tools, maybe hold off on upgrading to a 50-series card for a few more months until PyTorch stable and the major repos fully support CUDA 12.8+.