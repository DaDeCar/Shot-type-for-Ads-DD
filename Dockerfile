FROM nvidia/cuda:11.3.0-cudnn8-runtime-ubuntu20.04 as base

# Install some packages
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3.8-dev \
    python3-pip \
    ffmpeg \
    libsm6 \
    libxext6 \
    vim \
    wget \
    curl

# Add a non-root user
RUN useradd -ms /bin/bash app
USER app

# Setup some paths
ENV PYTHONPATH=/home/app/.local/lib/python3.8/site-packages:/home/app/src
ENV PATH=$PATH:/home/app/.local/bin

# Install the python packages for this new user
ADD requirements.txt .
RUN pip3 install -r requirements.txt



# Tensorflow (and Keras) with GPU support
RUN pip3 install tensorflow-gpu==2.8.0

# PyTorch GPU 1.10
#RUN pip3 install torch==1.10.0+cu111 torchvision==0.11.0+cu111 torchaudio==0.10.0 -f https://download.pytorch.org/whl/torch_stable.html

# Detectron2 for PyTorch 1.10 with CUDA support
#RUN pip3 install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu113/torch1.10/index.html

WORKDIR /home/app
