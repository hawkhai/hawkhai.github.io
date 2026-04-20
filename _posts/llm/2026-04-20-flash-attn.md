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
layoutclear: false
---

flash-attn 难装，不是它“设计复杂”，而是它强绑定 GPU + CUDA + PyTorch + 编译链版本，任何一个不一致就直接炸。


## 安装 Python3.11

```
# 安装依赖（必须）
sudo apt update
sudo apt install -y \
    build-essential \
    zlib1g-dev \
    libncurses5-dev \
    libgdbm-dev \
    libnss3-dev \
    libssl-dev \
    libreadline-dev \
    libffi-dev \
    wget

sudo apt install -y \
    build-essential \
    libbz2-dev libssl-dev libffi-dev \
    libreadline-dev zlib1g-dev libsqlite3-dev \
    libsqlite3-dev liblzma-dev tk-dev

sudo chown -R $(whoami):$(whoami) /data

# 下载 Python 3.11
cd /data
wget https://www.python.org/ftp/python/3.11.9/Python-3.11.9.tgz
tar -xvf Python-3.11.9.tgz
cd Python-3.11.9

# 编译安装（关键）
cd /data/Python-3.11.9
./configure --prefix=/data/python/python311 --enable-optimizations
make -j$(nproc)
make install

/data/python/python311/bin/python3.11

vim ~/.bashrc
export PATH=/data/python/python311/bin:$PATH # x:
source ~/.bashrc # 生效
which python3 # /data/python/python311/bin/python3
python3 -V # Python 3.11.9

# pip & venv 初始化
python3 -m ensurepip
python3 -m pip install --upgrade pip

mkdir -p /data/pip_cache
export PIP_CACHE_DIR=/data/pip_cache
# .bashrc
export PIP_CACHE_DIR=/data/pip_cache

# 创建统一虚拟环境目录
mkdir -p /data/venv
python3 -m venv /data/venv/base
source /data/venv/base/bin/activate

# 查看当前目录下每个子文件夹大小（推荐）
cd /data/
du -h --max-depth=1
```


## flash-attn

```
# Python 3.11（OK）
deactivate
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
```

```
pip install torch==2.5.0 torchvision==0.20.0 torchaudio==2.5.0 \
    --index-url https://download.pytorch.org/whl/cu121

# 2.5.0 12.1
python -c "import torch; print(torch.__version__, torch.version.cuda)"

pip install ninja setuptools wheel packaging cmake --index-url https://mirrors.aliyun.com/pypi/simple/
pip install flash-attn==2.5.8 --no-build-isolation -v --index-url https://mirrors.aliyun.com/pypi/simple/
pip install flash_attn-2.6.3+cu121torch2.5-cp311-linux_x86_64.whl

python -c "import flash_attn; print('flash-attn OK')"
pip install vllm

# 2. 如果还是 11.5，让我们下载并安装 CUDA 12.1
wget https://developer.download.nvidia.com/compute/cuda/12.1.1/local_installers/cuda_12.1.1_530.30.02_linux.run
# 3. 安装 CUDA 12.1（只安装工具包）
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
```

```
source /data/venv/base/bin/activate
cd /data/pythonx/
python3 kremotek.py downcode
python3 kremotek.py download code_mytts.json removex

cp -a /data/explore/mytts/nano-qwen3tts-vllm/examples/. \
    /data/nano-qwen3tts-vllm/examples/
cp -a /data/explore/mytts/nano-qwen3tts-vllm/nano-qwen3tts-vllm/. \
    /data/nano-qwen3tts-vllm/nano-qwen3tts-vllm/


nvidia-smi
watch -n 1 nvidia-smi

cp -a /data/nano-qwen3tts-vllm/output/. /data/explore/mytts/nano-qwen3tts-vllm/output/
```

```
python examples/custom_voice_example.py --model-path Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice \
    --text "人工智能技术的发展日新月异，深度学习模型在语音合成领域取得了突破性进展。现代文本转语音系统能够生成自然流畅的语音，音质接近真人水平。通过大规模预训练和精细调优，这些模型可以准确把握语言的韵律节奏，表达丰富的情感色彩。未来随着算力提升和算法优化，语音合成技术将更加智能高效，为各行各业带来更多创新应用场景。" \
    --speaker Vivian --language Chinese
```


## 验证一下

```
cd /data/nano-qwen3tts-vllm
export UV_CACHE_DIR=/data/uvcache/.cache/uv
source .venv/bin/activate
which python
which pip
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
python -c "import flash_attn; print(f'Flash Attention: {flash_attn.__version__}')"
"

Python: 3.11.9 (main, Apr 16 2026, 17:55:20) [GCC 11.4.0]
PyTorch: 2.5.0+cu121
CUDA available: True
CUDA version: 12.1
GPU count: 1
GPU 0: NVIDIA L4
Flash Attention: 2.5.8
```



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2026-04-20-flash-attn.md.js" %}'></script></p>
<font class='ref_snapshot'>参考资料快照</font>

- [https://www.python.org/ftp/python/3.11.9/Python-3.11.9.tgz]({% include relrefx.html url="/backup/2026-04-20-flash-attn.md/www.python.org/0ad48dc9.tgz" %})
- [https://download.pytorch.org/whl/cu121]({% include relrefx.html url="/backup/2026-04-20-flash-attn.md/download.pytorch.org/3719994a.html" %})
- [https://developer.download.nvidia.com/compute/cuda/12.1.1/local_installers/cuda_12.1.1_530.30.02_linux.run]({% include relrefx.html url="/backup/2026-04-20-flash-attn.md/developer.download.nvidia.com/1081b707.run" %})
