from tensorflow.keras.models import load_model
import cv2
import numpy as np
import os

# Load your newly trained model
MODEL_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "disaster_model.h5"
)

model = load_model(MODEL_PATH, compile=False)

# IMPORTANT:
# Check train_data.class_indices if predictions seem reversed
classes = ["fire", "flood"]

def predict_disaster(image_path):
    img = cv2.imread(image_path)

    if img is None:
        return {
            "disaster": "UNKNOWN",
            "confidence": 0.0
        }

    img = cv2.resize(img, (224, 224))
    img = img.astype("float32") / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img, verbose=0)

    predicted_index = np.argmax(prediction)
    predicted_class = classes[predicted_index]
    confidence = float(np.max(prediction))

    return {
        "disaster": predicted_class.upper(),
        "confidence": round(confidence * 100, 2)
    }