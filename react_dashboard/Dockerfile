FROM python:3.11-slim

WORKDIR /app

ENV PIP_NO_CACHE_DIR=1 \
    PIP_DEFAULT_TIMEOUT=200 \
    PIP_RETRIES=10

COPY requirements.txt .

RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
EXPOSE 8501