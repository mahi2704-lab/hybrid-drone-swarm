import os
import json
import time
import random
import hashlib
from datetime import datetime

# ---------- FILE PATH ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "swarm_state.json")

print("=== Hybrid Edge–Cloud Digital Twin with AI + Blockchain ===")


# ---------- BLOCKCHAIN CLASS ----------
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = (
            str(self.index)
            + str(self.timestamp)
            + json.dumps(self.data)
            + str(self.previous_hash)
        )
        return hashlib.sha256(block_string.encode()).hexdigest()


# ---------- BLOCKCHAIN ----------
blockchain = []

# Create genesis block
genesis = Block(
    0,
    str(datetime.now()),
    {"message": "Genesis Block"},
    "0"
)

blockchain.append(genesis)


# ---------- AI MODEL ----------
def ai_detect_survivor(temperature):
    """
    Simulated AI model:
    Higher temperature = higher probability of survivor
    """
    confidence = round(random.uniform(0.5, 0.99), 2)

    if temperature > 37.5 and confidence > 0.6:
        return True, confidence
    else:
        return False, confidence


# ---------- DRONE CLASS ----------
class Drone:
    def __init__(self, drone_id):
        self.drone_id = drone_id

    def sense_temperature(self):
        return round(random.uniform(32, 40), 2)

    def create_block(self, data):
        previous_block = blockchain[-1]

        new_block = Block(
            len(blockchain),
            str(datetime.now()),
            data,
            previous_block.hash
        )

        blockchain.append(new_block)

        return new_block.hash

    def act(self):
        temperature = self.sense_temperature()

        survivor_detected, confidence = ai_detect_survivor(temperature)

        block_data = {
            "drone_id": self.drone_id,
            "temperature": temperature,
            "survivor_detected": survivor_detected,
            "confidence": confidence
        }

        block_hash = self.create_block(block_data)

        print(
            f"[EDGE AI] Drone {self.drone_id} | "
            f"Temp: {temperature} | "
            f"Survivor: {survivor_detected} | "
            f"Confidence: {confidence} | "
            f"Block: {block_hash[:10]}..."
        )

        return {
            "drone_id": self.drone_id,
            "temperature": temperature,
            "survivor_detected": survivor_detected,
            "confidence": confidence,
            "block_hash": block_hash
        }


# ---------- CREATE DRONES ----------
drones = [
    Drone(1),
    Drone(2),
    Drone(3)
]

step = 0

# ---------- DIGITAL TWIN LOOP ----------
while True:

    print(f"\n--- Simulation Step {step} ---")

    drone_data = []
    survivor_count = 0

    for drone in drones:
        result = drone.act()

        drone_data.append(result)

        if result["survivor_detected"]:
            survivor_count += 1

    # ---------- WRITE TO CLOUD FILE ----------
    swarm_state = {

        "active_drones": len(drones),

        "survivors_detected": survivor_count,

        "status": "Running",

        "step": step,

        "blockchain_length": len(blockchain),

        "drones": drone_data
    }

    with open(DATA_FILE, "w") as f:
        json.dump(swarm_state, f, indent=4)

    step += 1

    time.sleep(2)
