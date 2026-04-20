---
layout: post
title: "工作笔记 -- flash-attn"
author:
location: "twiki"
categories: ["工作笔记"]
tags: ["编程", "工作笔记"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
archived:
date: 2025-06-24 09:52:22 +0800
layoutclear: false
---




# flash-attn 难装，不是它“设计复杂”，而是它强绑定 GPU + CUDA + PyTorch + 编译链版本，任何一个不一致就直接炸。
# Python 3.11（OK）
deactivate
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate

pip install torch==2.5.0 torchvision==0.20.0 torchaudio==2.5.0 \
  --index-url https://download.pytorch.org/whl/cu121
  
# 2.5.0 12.1
python -c "import torch; print(torch.__version__, torch.version.cuda)"

pip install -U pip setuptools wheel packaging ninja --index-url https://mirrors.aliyun.com/pypi/simple/

pip install ninja setuptools wheel packaging cmake --index-url https://mirrors.aliyun.com/pypi/simple/
pip install flash-attn==2.6.3 --no-build-isolation -v
pip uninstall flash-attn -y
pip install flash-attn==2.5.8 --no-build-isolation -v --index-url https://mirrors.aliyun.com/pypi/simple/
pip install flash_attn-2.6.3+cu121torch2.5-cp311-linux_x86_64.whl

python -c "import flash_attn; print('flash-attn OK')"
pip install vllm

# 2. 如果还是 11.5，让我们下载并安装 CUDA 12.1
wget https://developer.download.nvidia.com/compute/cuda/12.1.1/local_installers/cuda_12.1.1_530.30.02_linux.run
# 3. 安装 CUDA 12.1 (只安装工具包)
sudo TMPDIR=/data/tmp_cuda sh cuda_12.1.1_530.30.02_linux.run --silent --toolkit

sudo rm -rf /usr/local/cuda
sudo rm -rf /usr/local/cuda-13.0
sudo ln -s /usr/local/cuda-12.1 /usr/local/cuda

export CUDA_HOME=/usr/local/cuda
export PATH=$CUDA_HOME/bin:$PATH
export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH

which nvcc
nvcc -V


nvcc -V
python -c "import torch; print(torch.__version__, torch.version.cuda)"
which nvcc

python examples/custom_voice_example.py --model-path Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice --text "Hello world" --speaker Vivian


wget https://raw.githubusercontent.com/hawkhai/nano-qwen3tts-vllm/main/nano-qwen3tts-vllm/interface.py -O nano-qwen3tts-vllm/interface.py
wget https://raw.githubusercontent.com/hawkhai/nano-qwen3tts-vllm/main/examples/custom_voice_example.py      -O examples/custom_voice_example.py

source /data/venv/base/bin/activate
cd /data/pythonx/
python3 kremotek.py downcode
python3 kremotek.py download code_mytts.json removex
  ⏱️  Performance Metrics:
    Pure Inference Time: 13.595s
    Decode Time:         0.668s
    I/O Time:            0.009s
    Total Time:          14.272s
    Audio Duration:      38.880s
    RTF (Real-Time Factor): 0.350x
    Throughput:          11.2 chars/sec

cp -a /data/explore/mytts/nano-qwen3tts-vllm/examples/. \
     /data/nano-qwen3tts-vllm/examples/
cp -a /data/explore/mytts/nano-qwen3tts-vllm/nano-qwen3tts-vllm/. \
     /data/nano-qwen3tts-vllm/nano-qwen3tts-vllm/

nvidia-smi

cp -a /data/nano-qwen3tts-vllm/output/. /data/explore/mytts/nano-qwen3tts-vllm/output/ 
     
	 
	 
	 



deactivate
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate

pip install torch torchvision torchaudio \
  --index-url https://download.pytorch.org/whl/cu121 \
  --extra-index-url https://mirrors.aliyun.com/pypi/simple/

python -c "import torch; print(torch.cuda.is_available())"
pip install -U pip setuptools wheel packaging ninja psutil --index-url https://mirrors.aliyun.com/pypi/simple/
pip install flash-attn==2.8.3 --no-build-isolation --index-url https://mirrors.aliyun.com/pypi/simple/



python examples/custom_voice_example.py   --model-path Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice   --text "人工智能技术的发展日新月异，深度学习模型在语音合成领域取得了突破性进展。现代文本转语音系统能够生成自然流畅的语音，音质接近真人水平。通过大规模预训练和精细调优，这些模型可以准确把握语言的韵律节奏，表达丰富的情感色彩。未来随着算力提升和算法优化，语音合成技术将更加智能高效，为各行各业带来更多创新应用场景。"   --speaker Vivian   --language Chinese







# 全新尝试 Python 3.12, CUDA 12.4, PyTorch 2.5
pip install uv --index-url https://mirrors.aliyun.com/pypi/simple/
cd /data/nano-qwen3tts-vllm
export UV_CACHE_DIR=/data/uvcache/.cache/uv

uv python install 3.12
uv python pin 3.12

uv venv --python 3.12
source .venv/bin/activate

uv pip install torch==2.5.0 torchvision==0.20.0 torchaudio==2.5.0 \
  --index-url https://download.pytorch.org/whl/cu121 \
  --extra-index-url https://mirrors.aliyun.com/pypi/simple/

uv pip install setuptools wheel ninja packaging --index-url https://mirrors.aliyun.com/pypi/simple/

# Example: Python 3.12, CUDA 12.4, PyTorch 2.5
uv pip install flash-attn==2.6.3 --no-build-isolation --index-url https://mirrors.aliyun.com/pypi/simple/

# 1. 创建符号链接让 flash-attn 找到 nvcc
sudo mkdir -p /usr/local/cuda/bin
sudo ln -sf /usr/lib/nvidia-cuda-toolkit/bin/nvcc /usr/local/cuda/bin/nvcc
sudo ln -sf /usr/lib/nvidia-cuda-toolkit/lib64 /usr/local/cuda/lib64

# 2. 设置 CUDA_HOME
export CUDA_HOME=/usr/local/cuda
export PATH=$CUDA_HOME/bin:$PATH
export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH

# 3. 验证 nvcc 位置
which nvcc
ls -la /usr/local/cuda/bin/nvcc

# 4. 尝试安装 flash-attn
uv pip install flash-attn==2.6.3 --no-build-isolation --index-url https://mirrors.aliyun.com/pypi/simple/

# 5. 如果还是失败，直接测试 TTS
uv run python examples/custom_voice_example.py --model-path Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice --text "Hello world" --speaker Vivian



# 1. 检查当前 nvcc 版本
nvcc -V

# 2. 如果还是 11.5，让我们下载并安装 CUDA 12.1
wget https://developer.download.nvidia.com/compute/cuda/12.1.1/local_installers/cuda_12.1.1_530.30.02_linux.run


# 3. 安装 CUDA 12.1 (只安装工具包)
sudo TMPDIR=/data/tmp_cuda sh cuda_12.1.1_530.30.02_linux.run --silent --toolkit

# 4. 更新环境变量
export CUDA_HOME=/usr/local/cuda-12.1
export PATH=$CUDA_HOME/bin:$PATH
export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH

# 5. 验证新版本
$CUDA_HOME/bin/nvcc --version

# 6. 安装 flash-attn
uv pip install flash-attn --no-build-isolation --prefer-binary --index-url https://mirrors.aliyun.com/pypi/simple/



# 1. 检查系统信息
uname -m
cat /etc/os-release | grep VERSION_ID

# 3. 安装 CUDA 12.1 (只安装工具包，不安装驱动)
sudo TMPDIR=/data/tmp_cuda sh cuda_12.1.1_530.30.02_linux.run --silent --toolkit
sudo rm -rf /tmp/*
mkdir -p /data/tmp_cuda
sudo TMPDIR=/data/tmp_cuda sh cuda_12.1.1_530.30.02_linux.run --silent --toolkit


# 4. 设置环境变量
export CUDA_HOME=/usr/local/cuda-12.1
export PATH=$CUDA_HOME/bin:$PATH
export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH

# 5. 验证安装
$CUDA_HOME/bin/nvcc --version

# 6. 安装 flash-attn
uv pip install flash-attn==2.6.3 --no-build-isolation --index-url https://mirrors.aliyun.com/pypi/simple/

# 7. 验证 flash-attn
python -c "import flash_attn; print(f'Flash Attention: {flash_attn.__version__}')"





uv run python examples/custom_voice_example.py --model-path Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice --text "Hello world" --speaker Vivian

# 1. 卸载当前 PyTorch
uv pip uninstall torch torchaudio

# 2. 安装 PyTorch 2.4.0（可能与 flash-attn wheel 更兼容）
uv pip install torch==2.4.0 torchaudio==2.4.0 \
  --index-url https://download.pytorch.org/whl/cu121 \
  --extra-index-url https://mirrors.aliyun.com/pypi/simple/

# 3. 验证 PyTorch 版本
python -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA: {torch.version.cuda}')"

# 4. 重新安装 flash-attn
uv pip install /data/explore/mytts/qwen/flash_attn-2.6.3+cu121torch2.4-cp312-cp312-linux_x86_64.whl

# 5. 验证 flash-attn
python -c "import flash_attn; print(f'Flash Attention: {flash_attn.__version__}')"

# 6. 测试 TTS
uv run python examples/custom_voice_example.py --model-path Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice --text "Hello world" --speaker Vivian

------

# 1. 卸载当前版本
uv pip uninstall torch torchaudio

# 2. 安装 PyTorch 2.5.0 with CUDA 12.4
uv pip install torch==2.5.0 torchaudio==2.5.0 \
  --index-url https://download.pytorch.org/whl/cu121 \
  --extra-index-url https://mirrors.aliyun.com/pypi/simple/

# 3. 验证 CUDA 版本
python -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA: {torch.version.cuda}')"

# 4. 安装对应的 flash-attn (PyTorch 2.5 + CUDA 12.4)
uv pip install /data/explore/mytts/qwen/flash_attn-2.6.3+cu121torch2.5-cp312-cp312-linux_x86_64.whl

# 5. 验证 flash-attn
python -c "import flash_attn; print(f'Flash Attention: {flash_attn.__version__}')"

# 6. 测试 TTS
uv run python examples/custom_voice_example.py --model-path Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice --text "Hello world" --speaker Vivian

## 尝试编译这玩意。
# 1. 卸载当前的 flash-attn
uv pip uninstall flash-attn

# 2. 安装构建依赖
uv pip install setuptools wheel ninja packaging --index-url https://mirrors.aliyun.com/pypi/simple/

# 3. 验证编译环境
python -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA: {torch.version.cuda}'); print(f'GPU available: {torch.cuda.is_available()}')"


# 卸载当前 PyTorch
uv pip uninstall torch torchaudio

# 重新安装 PyTorch 2.5.0 with CUDA 12.4
uv pip install torch==2.5.0 torchaudio==2.5.0 \
  --index-url https://download.pytorch.org/whl/cu121 \
  --extra-index-url https://mirrors.aliyun.com/pypi/simple/

# 验证版本
python -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA: {torch.version.cuda}')"


# 检查 CUDA 是否在系统路径中
echo $PATH
find /usr -name nvcc 2>/dev/null
find /opt -name nvcc 2>/dev/null

# 检查 PyTorch 是否能找到 CUDA 编译器
python -c "import torch; print(torch.cuda.cudnn_version()); print(torch.cuda.version())"



# 检查 CUDA 编译器位置
echo $PATH
find /usr -name nvcc 2>/dev/null
find /opt -name nvcc 2>/dev/null
find /usr/local -name nvcc 2>/dev/null

# 检查 NVIDIA 驱动和 CUDA 运行时
nvidia-smi
python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}'); print(f'CUDA version: {torch.version.cuda}'); print(f'cuDNN version: {torch.backends.cudnn.version()}')"





# 检查必要的编译工具
which gcc
gcc --version
which nvcc
nvcc --version


# 1. 检查系统包管理器
which apt-get

# 2. 更新包列表
sudo apt-get update

# 3. 安装 CUDA 工具包 (12.4 版本)
sudo apt-get install nvidia-cuda-toolkit

# 4. 设置 CUDA_HOME 环境变量
export CUDA_HOME=/usr/local/cuda
export PATH=$CUDA_HOME/bin:$PATH
export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH

# 5. 验证 nvcc 安装
nvcc --version

# 6. 永久保存环境变量到 .bashrc
echo 'export CUDA_HOME=/usr/local/cuda' >> ~/.bashrc
echo 'export PATH=$CUDA_HOME/bin:$PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc





# 尝试直接安装 flash-attn（让 PyTorch 处理 CUDA 编译）
uv pip install flash-attn==2.6.3 --no-build-isolation --index-url https://mirrors.aliyun.com/pypi/simple/
# 备选方案：设置 CUDA_HOME 环境变量
export CUDA_HOME=$(python -c "import torch; import os; cuda_path = torch.__file__.replace('__init__.py', 'lib'); print(os.path.dirname(cuda_path))" 2>/dev/null || echo "")
echo "CUDA_HOME: $CUDA_HOME"

# 然后再次尝试安装
uv pip install flash-attn==2.6.3 --no-build-isolation --index-url https://mirrors.aliyun.com/pypi/simple/




# 克隆 flash-attn 源码
git clone https://github.com/Dao-AILab/flash-attention.git
cd flash-attention

# 切换到 v2.6.3 标签
git checkout v2.6.3

# 开始编译（这可能需要 10-30 分钟）
cd csrc/flash_attn
uv pip install . --no-build-isolation --index-url https://mirrors.aliyun.com/pypi/simple/



# 1. 找到 nvcc 的实际位置
which nvcc
find /usr -name nvcc -type f 2>/dev/null
find /opt -name nvcc -type f 2>/dev/null

# 2. 设置 CUDA_HOME 指向实际位置
export CUDA_HOME=$(dirname $(dirname $(which nvcc)))
echo "CUDA_HOME set to: $CUDA_HOME"
export PATH=$CUDA_HOME/bin:$PATH

# 3. 验证 nvcc
$CUDA_HOME/bin/nvcc --version

# 4. 尝试编译 flash-attn（即使 CUDA 版本不匹配，也许能工作）
uv pip install flash-attn==2.6.3 --no-build-isolation --index-url https://mirrors.aliyun.com/pypi/simple/


# 1. 正确设置 CUDA_HOME
export CUDA_HOME=/usr/lib/nvidia-cuda-toolkit
export PATH=$CUDA_HOME/bin:$PATH
export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH

# 2. 验证环境
echo "CUDA_HOME: $CUDA_HOME"
$CUDA_HOME/bin/nvcc --version

# 3. 降级到 PyTorch 2.4.0 with CUDA 12.1 (兼容 CUDA 11.5)
uv pip uninstall torch torchaudio
uv pip install torch==2.4.0 torchaudio==2.4.0 \
  --index-url https://download.pytorch.org/whl/cu121 \
  --extra-index-url https://mirrors.aliyun.com/pypi/simple/

# 4. 验证 PyTorch
python -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA: {torch.version.cuda}')"

# 5. 尝试编译 flash-attn
uv pip install flash-attn==2.0.9 --no-build-isolation --index-url https://mirrors.aliyun.com/pypi/simple/



# 1. 克隆 flash-attn 源码
git clone https://github.com/Dao-AILab/flash-attention.git
cd flash-attention

# 2. 切换到 v2.0.9 标签（可能支持 CUDA 11.5）
git checkout v2.0.9

# 3. 确保环境变量正确
export CUDA_HOME=/usr/lib/nvidia-cuda-toolkit
export PATH=$CUDA_HOME/bin:$PATH
export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH

# 4. 验证环境
echo "CUDA_HOME: $CUDA_HOME"
nvcc --version
python -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'CUDA: {torch.version.cuda}')"

# 5. 开始编译（这可能需要 10-30 分钟）
uv pip install . --no-build-isolation --index-url https://mirrors.aliyun.com/pypi/simple/

# 6. 如果编译成功，验证安装
cd ..
python -c "import flash_attn; print(f'Flash Attention: {flash_attn.__version__}')"

# 7. 测试 TTS
uv run python examples/custom_voice_example.py --model-path Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice --text "Hello world" --speaker Vivian


















#uv venv --python 3.10.12
uv venv activate
# 1. torch
uv pip install torch==2.5.0 torchvision==0.20.0 torchaudio==2.5.0 \
  --index-url https://download.pytorch.org/whl/cu121 \
  --extra-index-url https://mirrors.aliyun.com/pypi/simple/
# 2. flash-attn
uv pip install setuptools wheel ninja packaging --index-url https://mirrors.aliyun.com/pypi/simple/
uv pip install flash-attn==2.6.3 --no-build-isolation --index-url https://mirrors.aliyun.com/pypi/simple/



source /data/venv/base/bin/activate
sudo rm -rf /home/yangquanhai/.cache/uv/
cd /data/nano-qwen3tts-vllm
export UV_CACHE_DIR=/data/uvcache/.cache/uv
uv sync --index-url https://mirrors.aliyun.com/pypi/simple/

cd /data/nano-qwen3tts-vllm
export UV_CACHE_DIR=/data/uvcache/.cache/uv
source .venv/bin/activate
which python
which pip

# 安装基础依赖
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 -i https://mirrors.aliyun.com/pypi/simple/
# 安装 Flash Attention
pip install flash-attn==2.6.3 --no-build-isolation -i https://mirrors.aliyun.com/pypi/simple/
# 或者使用预编译轮子
pip install https://github.com/mjun0812/flash-attention-prebuild-wheels/releases/download/v0.0.0/flash_attn-2.6.3+cu121torch2.10-cp310-cp310-linux_x86_64.whl --no-build-isolation

# Python 3.10.12, PyTorch 2.10.0+cu121, CUDA 12.8, GPU: NVIDIA L4
python -m pip install flash-attn==2.6.3 --no-build-isolation -i https://mirrors.aliyun.com/pypi/simple/

python examples/custom_voice_example.py --model-path Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice --text "Hello world" --speaker Vivian

```

```
python3 -c "
import torch
import sys
print(f'Python: {sys.version}')
print(f'PyTorch: {torch.__version__}')
print(f'CUDA available: {torch.cuda.is_available()}')
if torch.cuda.is_available():
    print(f'CUDA version: {torch.version.cuda}')
    print(f'GPU count: {torch.cuda.device_count()}')
    for i in range(torch.cuda.device_count()):
        print(f'GPU {i}: {torch.cuda.get_device_name(i)}')
"

Python: 3.11.9 (main, Apr 16 2026, 17:55:20) [GCC 11.4.0]
PyTorch: 2.11.0+cu130
CUDA available: True
CUDA version: 13.0
GPU count: 1
GPU 0: NVIDIA L4
```
