from tensorflow.keras.models import load_model

model = load_model("drone_disaster_cnn.h5")
model.summary()