# ============================================================
# CNN PREDICTION FILE (SAFE VERSION WITH FALLBACK)
# ============================================================

import numpy as np
import tensorflow as tf
import os

MODEL_PATH = "ai_server/cnn_drone_model.h5"

model = None

# Try loading model
if os.path.exists(MODEL_PATH):

    print("Loading CNN model...")
    model = tf.keras.models.load_model(MODEL_PATH)

else:

    print("CNN model not found. Using fallback logic.")


def predict_decision(drone_data):

    battery = drone_data.get("battery", 50)

    lidar = drone_data.get("lidar", {
        "front": 50,
        "left": 50,
        "right": 50,
        "rear": 50
    })

    front = lidar.get("front", 50)
    left = lidar.get("left", 50)
    right = lidar.get("right", 50)
    rear = lidar.get("rear", 50)

    # =====================================================
    # IF MODEL EXISTS → USE CNN
    # =====================================================
    if model is not None:

        features = [battery, front, left, right, rear]

        X = np.array(features).reshape(1, 5, 1)

        prediction = model.predict(X, verbose=0)

        class_id = int(np.argmax(prediction))

        confidence = float(np.max(prediction))

        if class_id == 0:
            decision = "RETURN_TO_BASE"
        elif class_id == 1:
            decision = "CONTINUE_MISSION"
        else:
            decision = "OPTIMAL"

        return decision, round(confidence, 2)

    # =====================================================
    # FALLBACK LOGIC (NO MODEL)
    # =====================================================
    else:

        if battery < 25:
            return "RETURN_TO_BASE", 0.95

        elif front < 20:
            return "AVOID_OBSTACLE", 0.90

        else:
            return "CONTINUE_MISSION", 0.85
