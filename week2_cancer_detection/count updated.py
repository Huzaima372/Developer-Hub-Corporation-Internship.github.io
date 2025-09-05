import os

# Tumhara folder path
FOLDER_PATH = r"C:/Users/ABC/Desktop/ML PROJ_2/cancer_subset_500"
# Benign folder
benign_path = os.path.join(FOLDER_PATH, "benign")
benign_count = len([f for f in os.listdir(benign_path) if f.endswith(".png")])

# Malignant folder
malignant_path = os.path.join(FOLDER_PATH, "malignant")
malignant_count = len([f for f in os.listdir(malignant_path) if f.endswith(".png")])

print(f"✅ Benign images: {benign_count}")
print(f"✅ Malignant images: {malignant_count}")
print(f"✅ Total images: {benign_count + malignant_count}")
