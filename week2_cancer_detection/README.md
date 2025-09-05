# 🌟PROJECT 2: Cancer Detection Using CNN & VGG16

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)
![Keras](https://img.shields.io/badge/Keras-DeepLearning-red.svg)
![Scikit-Learn](https://img.shields.io/badge/ScikitLearn-ML-yellow.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-green.svg)
![VS Code](https://img.shields.io/badge/Editor-VSCode-purple.svg)


---

## 📌 Objective

This project explores **Cancer Detection** using **Convolutional Neural Networks (CNNs)** and **Transfer Learning (VGG16)**.
The main goal is to compare the performance of a **custom CNN model** with a **pre-trained VGG16 model** on a small subset of histopathological cancer images.

---

## 📂 Dataset

* **Source:** Breast Cancer Histopathological Dataset (subset of \~500 images).
* **Classes:**

  * **Benign** (non-cancerous)
  * **Malignant** (cancerous)
* **Split:** 80% Training, 20% Validation.
* **Preprocessing:**

  * Resized to **128×128** pixels
  * Normalized pixel values to **\[0,1]**

---

## 🧪 Models Implemented

### 🔹 Custom CNN

* 3 Convolutional layers with MaxPooling
* Fully Connected Layer + Dropout
* Sigmoid output for binary classification
* **Optimizer:** Adam (lr=0.001)
* **Loss Function:** Binary Crossentropy

### 🔹 Transfer Learning (VGG16)

* Pre-trained **VGG16** base (weights loaded locally, ImageNet-trained)
* Base layers **frozen** to retain pre-learned features
* Added custom dense layers with Dropout
* **Optimizer:** Adam (lr=0.0001)
* **Loss Function:** Binary Crossentropy

---

## 📊 Results & Graphs

* **Training & Validation Accuracy/Loss curves** plotted for both CNN & VGG16.
* VGG16 demonstrated **better performance** due to transfer learning.

---

## ▶️ Usage

### 1. Clone the repo

```bash
https://github.com/Huzaima372/Developer-Hub-Corporation-Internship.github.io/tree/main/week2_cancer_detection
```

### 2. Run the notebook/script

```bash
python cancer_detection.py
```

### 3. Single Image Prediction

Change the path in the script:

```python
test_image_path = r"cancer_subset_500\benign\example.png"
predict_single_image(vgg_model, test_image_path)
```

Example Output:

```
example.png --> Cancer Detected
```

---

## ⚙️ Tech Stack

* **Python** 🐍
* **TensorFlow / Keras**
* **Scikit-learn**
* **Matplotlib**
* **VS Code / Google Colab**

---

## ✅ Outcome

* Successfully trained a **custom CNN** and a **VGG16-based Transfer Learning model**.
* Transfer Learning achieved **higher accuracy** and generalization.
* Implemented **single image cancer prediction**.
* This project highlights the potential of **AI in medical image-based cancer detection**.
