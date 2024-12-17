FROM nvidia/cuda:12.5.0-devel-ubuntu22.04
# FROM python:3.11-slim
ARG LM_EVAL_HARNESS_VERSION=v0.4.6
ARG DEBIAN_FRONTEND=noninteractive

# The container should not rely on any external resources after it is built
RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash

RUN apt update && apt install -y git python3-pip python3-dev openjdk-21-jdk python-is-python3 wget curl git-lfs unzip


#RUN apt install -y git libsndfile1-dev tesseract-ocr espeak-ng python3 python3-pip ffmpeg build-essential

RUN python3 -m pip install --no-cache-dir --upgrade pip

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt


WORKDIR /app

