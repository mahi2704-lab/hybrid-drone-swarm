FROM python:3.10-slim

WORKDIR /app

# =========================
# SYSTEM DEPENDENCIES
# =========================
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# =========================
# INSTALL PYTHON DEPENDENCIES
# =========================
COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install \
    --no-cache-dir \
    --default-timeout=100 \
    --retries=15 \
    -r requirements.txt

# =========================
# COPY PROJECT FILES
# =========================
COPY . .

# =========================
# IMPORTANT: ENSURE DATASET IS INSIDE CONTAINER
# =========================
COPY dataset /app/dataset

# =========================
# PORT
# =========================
EXPOSE 8000

# =========================
# START FASTAPI
# =========================
CMD ["uvicorn", "ai_server.api:app", "--host", "0.0.0.0", "--port", "8000"]