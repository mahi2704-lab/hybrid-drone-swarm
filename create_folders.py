import os

base_path = "dataset"

splits = ["train", "val", "test"]
classes = ["flood", "fire", "earthquake", "safe"]

for split in splits:
    for cls in classes:
        path = os.path.join(base_path, split, cls)
        os.makedirs(path, exist_ok=True)

print("Dataset folder structure created successfully!")