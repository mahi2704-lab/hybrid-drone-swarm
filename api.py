from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import random
import time

from ai_service import predict_anomaly
from blockchain.blockchain_logger import create_block
from edge.edge_processor import edge_analyze
from cloud.firebase_sync import sync_to_cloud

app = FastAPI(
    title="Hybrid Edge-Cloud Multi-Agent Drone Swarm Framework",
    description="Secure AI-Based Disaster Response System using CNN, Edge Computing, Blockchain, Cloud Synchronization, and Real-Time Drone Monitoring.",
    version="1.0"
)

# Global memory table tracking your multi-agent swarm fleet coordinates
# This simulates live CNN tracker frames in your target sector (e.g., Chennai Coastal Zone)
fleet_mission_registry = {
    "mission_status": "SWARM_ACTIVE",
    "disaster_type": "Flood",
    "target_zone": "Chennai Coastal Zone",
    "detected_survivors": [
        {"id": "SVR_101", "lat": 13.0827, "lng": 80.2707, "cnn_confidence": 96.2, "source_drone": "Alpha"},
        {"id": "SVR_102", "lat": 13.0855, "lng": 80.2789, "cnn_confidence": 91.5, "source_drone": "Beta"},
        {"id": "SVR_103", "lat": 13.0792, "lng": 80.2641, "cnn_confidence": 94.8, "source_drone": "Gamma"}
    ]
}

# Data schema for incoming automation command
class RescueActivationPayload(BaseModel):
    disaster_type: str
    target_zone: str
    total_survivors: int
    verified_coordinates: List[Dict[str, float]]

@app.get("/")
def home():
    return {"message": "Hybrid Drone Swarm Backend Running"}

@app.get("/drone-status")
def drone_status():
    # RANDOM SYSTEM CONDITION
    mode = random.choice(["safe", "warning", "critical"])

    # SAFE CONDITIONS
    if mode == "safe":
        battery = random.randint(75, 100)
        signal = random.randint(75, 100)
        cpu = random.randint(20, 55)
        latency = random.randint(1, 7)
    # WARNING CONDITIONS
    elif mode == "warning":
        battery = random.randint(45, 70)
        signal = random.randint(45, 70)
        cpu = random.randint(60, 80)
        latency = random.randint(8, 12)
    # CRITICAL CONDITIONS
    else:
        battery = random.randint(10, 40)
        signal = random.randint(20, 45)
        cpu = random.randint(81, 95)
        latency = random.randint(13, 20)

    sensor_data = [battery, signal, cpu, latency]

    # Run your native framework modules
    anomaly_score = predict_anomaly(sensor_data)
    edge_status = edge_analyze(sensor_data)

    if edge_status == "CRITICAL":
        status = "CRITICAL DISASTER ALERT"
    elif edge_status == "WARNING":
        status = "WARNING"
    else:
        status = "OPERATIONAL"

    # Blockchain logging
    block = create_block({
        "battery": battery,
        "signal": signal,
        "cpu": cpu,
        "latency": latency,
        "anomaly_score": anomaly_score,
        "edge_status": edge_status,
        "status": status
    })

    # Cloud synchronization
    sync_to_cloud(block)

    # Dynamic target variance for your map integration
    for survivor in fleet_mission_registry["detected_survivors"]:
        survivor["lat"] += (random.random() - 0.5) * 0.001
        survivor["lng"] += (random.random() - 0.5) * 0.001

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
    """
    Automated Rescue Trigger: Verifies the CNN payload data, logs the activation event
    to the secure ledger chain, and dispatches responders.
    """
    if payload.total_survivors == 0:
        raise HTTPException(status_code=400, detail="Deployment Aborted: No active targets.")

    # Create an immutable block specifically tracking this mission initiation
    rescue_block = create_block({
        "event": "AUTOMATED_RESCUE_TRIGGERED",
        "target_zone": payload.target_zone,
        "survivors_dispatched": payload.total_survivors,
        "timestamp": time.time()
    })
    sync_to_cloud(rescue_block)

    return {
        "dispatch_status": "SUCCESSED",
        "allocated_rescue_units": max(1, payload.total_survivors // 2),
        "target_sector": payload.target_zone,
        "secure_receipt": rescue_block["hash"],
        "message": f"Rescue deployment confirmed for {payload.total_survivors} CNN-verified locations."
    }
