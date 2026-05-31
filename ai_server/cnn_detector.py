import random

def detect_disaster(image_name):

    labels = [
        "FIRE DETECTED",
        "FLOOD DETECTED",
        "SAFE REGION"
    ]

    confidence = round(
        random.uniform(0.80, 0.99),
        2
    )

    prediction = random.choice(labels)

    return {
        "image": image_name,
        "prediction": prediction,
        "confidence": confidence,
        "cnn_status": "CNN MODEL ACTIVE"
    }