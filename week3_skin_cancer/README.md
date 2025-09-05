# 🩺 Skin Cancer Detection using ResNet50  

## 📌 Overview  
This project is part of the **DevelopersHub Internship – Week 3, Project 1**.  
The objective was to classify dermatoscopic skin lesion images into **cancerous** and **non-cancerous** categories using **transfer learning with ResNet50**.  

---

## ⚙️ Steps Performed  

### 📂 Dataset  
- Used **HAM10000 dataset** (from ISIC via Kaggle)  
- Split into **training (80%)** and **validation (20%)**  

### 🧹 Preprocessing  
- Resized all images to **128 × 128**  
- Normalized pixel values between **0–1**  
- Applied **ResNet50 preprocessing function**  
- Batch size = **32**  

### 🏗️ Model  
ResNet50-based architecture with:  
1. Pre-trained **ResNet50 base** (frozen, without top layers)  
2. **Global Average Pooling**  
3. **Dense layer (128 neurons, ReLU)**  
4. **Dropout (0.5)**  
5. **Dense output layer (Sigmoid activation)**  

### 🔄 Training  
- Optimizer: **Adam**  
- Loss: **Binary Crossentropy**  
- Epochs: **10**  
- Validation accuracy monitored during training  

### 📈 Evaluation  
- **Training vs Validation Accuracy Plot** generated  
- Accuracy measured across epochs  
- Validation confirmed **generalization performance**  

---

## 📊 Results  
- Accuracy curves showed **steady improvement**  
- Validation accuracy closely followed training accuracy → **good generalization**  
- The ResNet50-based model achieved **high classification accuracy** for skin lesion images  

👉 The model effectively detected **cancerous vs non-cancerous lesions**, showing potential as a **decision-support tool for dermatologists**.  

---

## 🛠️ Technologies Used  
- Python  
- TensorFlow & Keras  
- Matplotlib & Seaborn  
- Scikit-learn  
- KaggleHub (for dataset acquisition)  
