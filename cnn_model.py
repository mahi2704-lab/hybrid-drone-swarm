import random

def cnn_predict(image=None):
    # Simulated CNN output
    disasters = ["FLOOD", "FIRE", "EARTHQUAKE", "NONE"]

    result = random.choice(disasters)

    confidence = round(random.uniform(0.7, 0.99), 2)

    return {
        "disaster": result,
        "confidence": confidence
    }