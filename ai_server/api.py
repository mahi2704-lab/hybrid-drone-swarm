from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Dict
import random
import time
import os

app = FastAPI(title="Hybrid Edge-Cloud Multi-Agent Drone Swarm Framework")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_ROOT = os.path.join(BASE_DIR, "dataset")

if os.path.exists(DATASET_ROOT):
    app.mount("/static-dataset", StaticFiles(directory=DATASET_ROOT), name="static")

# Core state registry
fleet_mission_registry = {
    "mission_status": "SWARM_ACTIVE",
    "disaster_type": "Flood",
    "target_zone": "Chennai Coastal Zone",
    "detected_survivors": [
        {"id": "SVR_101", "lat": 13.0827, "lng": 80.2707, "source_drone": "Alpha", "processed_file": ""},
        {"id": "SVR_102", "lat": 13.0855, "lng": 80.2789, "source_drone": "Beta", "processed_file": ""},
        {"id": "SVR_103", "lat": 13.0792, "lng": 80.2641, "source_drone": "Gamma", "processed_file": ""}
    ]
}


class RescueActivationPayload(BaseModel):
    disaster_type: str
    target_zone: str
    total_survivors: int
    verified_coordinates: List[Dict[str, float]]


@app.get("/drone-status")
def drone_status():
    from ai_service import predict_anomaly
    from blockchain.blockchain_logger import create_block
    from edge.edge_processor import edge_analyze
    from cloud.firebase_sync import sync_to_cloud

    # 1. DYNAMIC ENHANCEMENT: Randomly cycle between your dataset types
    disaster_profiles = [
        {"type": "Flood", "zone": "Chennai Coastal Zone"},
        {"type": "Earthquake", "zone": "Urban Sector 9"},
        {"type": "Wildfire", "zone": "Forest Region Alpha"}
    ]
    selected_profile = random.choice(disaster_profiles)
    fleet_mission_registry["disaster_type"] = selected_profile["type"]
    fleet_mission_registry["target_zone"] = selected_profile["zone"]

    disaster_folder_name = fleet_mission_registry["disaster_type"].lower()
    target_folder_path = os.path.join(DATASET_ROOT, disaster_folder_name)

    selected_image_filename = "Fallback_Frame.jpg"

    try:
        if os.path.exists(target_folder_path):
            valid_images = [f for f in os.listdir(target_folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            if valid_images:
                selected_image_filename = random.choice(valid_images)
    except Exception as e:
        print(f"Dataset reading loop issue: {e}")

    # Process core metrics
    mode = random.choice(["safe", "warning", "critical"])
    if mode == "safe":
        battery, signal, cpu, latency = random.randint(75, 100), random.randint(75, 100), random.randint(20,
                                                                                                         55), random.randint(
            1, 7)
    elif mode == "warning":
        battery, signal, cpu, latency = random.randint(45, 70), random.randint(45, 70), random.randint(60,
                                                                                                       80), random.randint(
            8, 12)
    else:
        battery, signal, cpu, latency = random.randint(10, 40), random.randint(20, 45), random.randint(81,
                                                                                                       95), random.randint(
            13, 20)

    sensor_data = [battery, signal, cpu, latency]
    anomaly_score = predict_anomaly(sensor_data)
    edge_status = edge_analyze(sensor_data)

    status = "OPERATIONAL"
    if edge_status == "CRITICAL":
        status = "CRITICAL DISASTER ALERT"
    elif edge_status == "WARNING":
        status = "WARNING"

    block = create_block({
        "battery": battery, "signal": signal, "cpu": cpu,
        "latency": latency, "anomaly_score": anomaly_score,
        "edge_status": edge_status, "status": status
    })
    sync_to_cloud(block)

    # 2. CNN SIMULATION ENHANCEMENT: Compute random bounded boxes for the frontend image canvas
    for survivor in fleet_mission_registry["detected_survivors"]:
        survivor["lat"] += (random.random() - 0.5) * 0.0004
        survivor["lng"] += (random.random() - 0.5) * 0.0004
        survivor["processed_file"] = f"{disaster_folder_name}/{selected_image_filename}"

        # Inject dynamic object coordinates simulating a real CNN inference output layer box
        survivor["cnn_confidence"] = round(random.uniform(92.5, 99.1), 1)
        survivor["bbox"] = {
            "top": random.randint(10, 30),
            "left": random.randint(15, 45),
            "width": random.randint(30, 50),
            "height": random.randint(35, 55)
        }

    return {
        "active_drones": random.randint(5, 15),
        "battery_level": battery,
        "signal_strength": signal,
        "cpu_usage": cpu,
        "edge_latency": latency,
        "anomaly_score": round(anomaly_score, 2),
        "edge_status": edge_status,
        "status": status,
        "block_hash": block["hash"],
        "timestamp": block["timestamp"],
        "mission_context": fleet_mission_registry
    }


@app.post("/api/v1/mission/initiate-rescue")
def initiate_rescue_operations(payload: RescueActivationPayload):
    from blockchain.blockchain_logger import create_block
    rescue_block = create_block({"event": "AUTOMATED_RESCUE_TRIGGERED", "timestamp": time.time()})
    return {"dispatch_status": "SUCCESS", "allocated_rescue_units": 2, "secure_receipt": rescue_block["hash"],
            "message": "Rescue deployment confirmed."}
