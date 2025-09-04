# Pneumonia Detection using CNN

## 📌 Overview
This project is part of the **DevelopersHub Internship - Week 3**.  
The objective was to detect **pneumonia from chest X-ray images** using a Convolutional Neural Network (CNN).

---

## ⚙️ Steps Performed
1. **Dataset**
   - Used Kaggle dataset: *Chest X-Ray Pneumonia*.
   - Images were split into `train`, `val`, and `test`.

2. **Preprocessing**
   - Resized images to **128x128**.
   - Normalized pixel values between 0–1.
   - Batch size = 32.

3. **Model**
   - CNN architecture with:
     - 2 Conv2D layers + MaxPooling
     - Dense hidden layer (128 neurons, ReLU)
     - Dropout (0.5)
     - Output: sigmoid (binary classification)

4. **Training**
   - Optimizer: Adam
   - Loss: Binary Crossentropy
   - Epochs: 10
   - Validation during training

5. **Evaluation**
   - ROC Curve & AUC Score
   - Confusion Matrix
   - Classification Report (Accuracy, Precision, Recall, F1-score)

---

## 📊 Results
- **ROC AUC**: > 0.90 (indicating strong pneumonia detection)
- **Confusion Matrix**: very few misclassifications
- **Classification Report**:
  - High **precision** & **recall** for both Normal and Pneumonia classes
  - Accuracy > 85%

👉 The **CNN model effectively detected pneumonia** from chest X-rays, making it suitable for assisting medical diagnosis.

---

## 🛠️ Technologies Used
- Python
- TensorFlow & Keras
- Pandas & NumPy
- Matplotlib & Seaborn
- Scikit-learn
- KaggleHub (for dataset)

---
