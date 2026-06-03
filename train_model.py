from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models

# Image preprocessing
datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    validation_split=0.2
)

# Training data
train_data = datagen.flow_from_directory(
    "dataset/train",
    target_size=(224, 224),
    batch_size=8,
    class_mode="categorical",
    subset="training"
)

# Validation data
val_data = datagen.flow_from_directory(
    "dataset/train",
    target_size=(224, 224),
    batch_size=8,
    class_mode="categorical",
    subset="validation"
)

# CNN Model
model = models.Sequential([
    layers.Input(shape=(224, 224, 3)),

    layers.Conv2D(32, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(64, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(128, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),

    layers.Flatten(),

    layers.Dense(128, activation="relu"),
    layers.Dropout(0.5),

    layers.Dense(2, activation="softmax")  # flood + fire
])

# Compile
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

# Train
history = model.fit(
    train_data,
    validation_data=val_data,
    epochs=10
)

# Save model
model.save("disaster_model.h5")

print("Training completed!")
print("Model saved as disaster_model.h5")