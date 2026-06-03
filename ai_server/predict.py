from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Load trained model
model = load_model("../disaster_model.h5")

# Test image
IMAGE_PATH = "../dataset/train/fire/fire1.jpeg"

# Load image
img = image.load_img(IMAGE_PATH, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = img_array / 255.0

# Predict
prediction = model.predict(img_array)

classes = ["fire", "flood"]

predicted_class = classes[np.argmax(prediction)]
confidence = np.max(prediction) * 100

print("\n===== DISASTER PREDICTION =====")
print("Prediction :", predicted_class.upper())
print("Confidence :", round(confidence, 2), "%")
print("==============================")