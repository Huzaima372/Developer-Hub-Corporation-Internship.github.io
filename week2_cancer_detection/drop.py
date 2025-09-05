import os
import random

# Path to existing folder
FOLDER_PATH = r"C:/Users/ABC/Desktop/ML PROJ_2/cancer_subset_500"

# Number of images you want per class
N = 250

# -----------------------------
# Process benign folder
# -----------------------------
benign_path = os.path.join(FOLDER_PATH, "benign")
benign_images = os.listdir(benign_path)

# Randomly select N images to keep
benign_keep = set(random.sample(benign_images, N))

# Delete the rest
for img in benign_images:
    if img not in benign_keep:
        os.remove(os.path.join(benign_path, img))

# -----------------------------
# Process malignant folder
# -----------------------------
malignant_path = os.path.join(FOLDER_PATH, "malignant")
malignant_images = os.listdir(malignant_path)

# Randomly select N images to keep
malignant_keep = set(random.sample(malignant_images, N))

# Delete the rest
for img in malignant_images:
    if img not in malignant_keep:
        os.remove(os.path.join(malignant_path, img))

print(f"✅ Updated folder '{FOLDER_PATH}' with exactly {N} benign and {N} malignant images.")
