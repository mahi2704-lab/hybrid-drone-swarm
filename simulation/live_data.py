import json
import random
import time
import os
import hashlib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

OUTPUT = os.path.join(BASE_DIR, "swarm_state.json")

DISASTER_TYPES = [
    "FIRE",
    "FLOOD",
    "SAFE"
]

while True:

    drones = []

    survivors = 0

    for i in range(1, 6):

        # ----------------------------
        # SIMULATED THERMAL SENSOR
        # ----------------------------

        thermal_temperature = random.randint(30, 120)

        # ----------------------------
        # CNN DETECTION
        # ----------------------------

        detected_disaster = random.choice(DISASTER_TYPES)

        confidence = round(random.uniform(0.75, 0.99), 2)

        # ----------------------------
        # SURVIVOR DETECTION
        # ----------------------------

        survivor = random.choice([0, 1])

        if survivor == 1:
            survivors += 1

        # ----------------------------
        # GPS + GIS LOCATION
        # ----------------------------

        latitude = round(13.0500 + random.uniform(0, 0.08), 6)

        longitude = round(80.0000 + random.uniform(0, 0.08), 6)

        # ----------------------------
        # DRONE TELEMETRY
        # ----------------------------

        battery = random.randint(35, 100)

        signal = random.randint(40, 100)

        cpu_usage = random.randint(20, 95)

        latency = round(random.uniform(1, 15), 2)

        # ----------------------------
        # BLOCKCHAIN HASH
        # ----------------------------

        raw_block = (
            f"{i}"
            f"{thermal_temperature}"
            f"{confidence}"
            f"{latitude}"
            f"{longitude}"
        )

        block_hash = hashlib.sha256(
            raw_block.encode()
        ).hexdigest()

        # ----------------------------
        # DRONE OBJECT
        # ----------------------------

        drones.append({

            "drone_id": f"DRONE-{i}",

            "latitude": latitude,

            "longitude": longitude,

            "thermal_temperature": thermal_temperature,

            "detected_disaster": detected_disaster,

            "cnn_confidence": confidence,

            "survivor_detected": survivor,

            "battery": battery,

            "signal_strength": signal,

            "cpu_usage": cpu_usage,

            "edge_latency": latency,

            "block_hash": block_hash
        })

    # ----------------------------
    # DIGITAL TWIN STATE
    # ----------------------------

    data = {

        "active_drones": 5,

        "survivors_detected": survivors,

        "blockchain_length": len(drones),

        "mission_status": "ACTIVE",

        "drones": drones
    }

    # ----------------------------
    # SAVE JSON
    # ----------------------------

    with open(OUTPUT, "w") as f:

        json.dump(data, f, indent=4)

    print("Digital Twin Updated")

    time.sleep(3)