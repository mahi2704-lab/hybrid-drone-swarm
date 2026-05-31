import numpy as np
from tensorflow.keras.models import load_model

# Load trained CNN model once
model = load_model("drone_anomaly_cnn.h5")


def predict_anomaly(sensor_data):

    try:
        # Convert to numpy array
        data = np.array(sensor_data, dtype=np.float32)

        # Normalize values
        data = data / 100.0

        # Reshape for CNN input
        data = data.reshape(1, len(sensor_data), 1)

        # Predict anomaly
        prediction = model.predict(data, verbose=0)

        # Extract score
        anomaly_score = float(prediction[0][0])

        return round(anomaly_score, 2)

    except Exception as e:
        print("Prediction Error:", e)
        return 0.0