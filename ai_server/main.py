from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

state = {
    "status": "IDLE",
    "disaster": "none",
    "victims": 0,
    "tick": 0
}

@app.get("/")
def home():
    return {"status": "AI Disaster Backend Running"}

@app.get("/start/{disaster}")
def start(disaster: str):

    state["status"] = "SWARM_ACTIVE"
    state["disaster"] = disaster
    state["victims"] = random.randint(3, 10)
    state["tick"] = 0

    return state


@app.get("/status")
def status():

    state["tick"] += 1

    # simulate changing conditions
    state["victims"] = max(1, state["victims"] - random.randint(0, 1))

    if state["tick"] > 5:
        state["status"] = "RESCUE_IN_PROGRESS"

    return state


@app.get("/detect")
def detect():

    # moving detections (fake motion)
    base_x = random.randint(100, 300)
    base_y = random.randint(80, 200)

    return {
        "detections": [
            {"x": base_x, "y": base_y, "confidence": random.randint(80, 99)},
            {"x": base_x + 50, "y": base_y + 40, "confidence": random.randint(75, 95)}
        ]

    }