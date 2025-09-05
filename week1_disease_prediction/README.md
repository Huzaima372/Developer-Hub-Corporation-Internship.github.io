
# ❤️ Heart Disease Prediction – Week 01

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)  
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange.svg)](https://scikit-learn.org/)  
[![Pandas](https://img.shields.io/badge/Pandas-Data--Analysis-green.svg)](https://pandas.pydata.org/)  
[![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-red.svg)](https://seaborn.pydata.org/)  
[![Dataset](https://img.shields.io/badge/Dataset-UCI%20Heart%20Disease-brightgreen.svg)](https://archive.ics.uci.edu/dataset/45/heart+disease)  

---

## 📌 Project Overview
This project applies **Machine Learning** techniques to the **UCI Heart Disease dataset** to predict whether a patient is at risk of heart disease.  

The workflow includes:  
✔️ Data Preprocessing (handling missing values, normalization, encoding)  
✔️ Exploratory Data Analysis (EDA)  
✔️ Model Training (Logistic Regression, Random Forest)  
✔️ Model Evaluation & Comparison  

---

## ⚙️ Installation
Make sure you have Python 3.x installed. Then, install the required dependencies:

```bash
pip install ucimlrepo pandas numpy matplotlib seaborn scikit-learn
````

---

## 📂 Dataset

* **Source**: [UCI Machine Learning Repository – Heart Disease Dataset](https://archive.ics.uci.edu/dataset/45/heart+disease)
* **Total Records**: 303
* **Features**:

  * Numerical: `age`, `trestbps` (resting blood pressure), `chol` (cholesterol), `thalach` (max heart rate), `oldpeak` (ST depression).
  * Categorical: `sex`, `cp` (chest pain type), `fbs` (fasting blood sugar), `restecg`, `exang` (exercise-induced angina), `slope`, `ca`, `thal`.
* **Target Variable**:

  * `1` → Heart disease present
  * `0` → No heart disease

---

## 🔧 Data Preprocessing

1. **Missing Values**

   * Columns `ca` and `thal` had missing values → filled using **median imputation**.

2. **Normalization**

   * Numerical features scaled between **0–1** using **MinMaxScaler**.

3. **Categorical Encoding**

   * Binary columns (`sex`, `fbs`, `exang`) → **Label Encoding**.
   * Multi-category columns (`cp`, `slope`, `thal`, `restecg`, `ca`) → **One-Hot Encoding**.

4. **Target Transformation**

   * Converted target values into binary: `1` for disease present, `0` otherwise.

---

## 📊 Exploratory Data Analysis (EDA)

### Dataset Statistics

* Shape: **303 rows × 14 features**
* No missing values after preprocessing.

### Correlation Heatmap

A heatmap was plotted to analyze relationships between features and target:

* Strong positive correlation: `cp`, `thalach` with target.
* Negative correlation: `oldpeak`, `exang`, `ca`.

---

## 🤖 Model Training

### Data Splitting

* Train-test split: **80% training, 20% testing**.

### Models Used

1. **Logistic Regression** – baseline linear model.
2. **Random Forest Classifier** – ensemble learning method.

---

## 📈 Model Evaluation

### Metrics Used

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

### Results

| Model               | Accuracy | Precision | Recall  | F1 Score |
| ------------------- | -------- | --------- | ------- | -------- |
| Logistic Regression | \~86.9%  | \~87.0%   | \~84.4% | \~0.871  |
| Random Forest       | \~88.5%  | \~89.0%   | \~87.5% | \~0.889  |

---

## ✅ Conclusion

* **Random Forest performed better** than Logistic Regression.
* Achieved **higher accuracy, recall, and F1-score**.
* Random Forest misclassified fewer patients (4 vs 5 by Logistic Regression).

👉 **Final Choice: Random Forest Classifier** for heart disease prediction.

---

## 📚 References

* [UCI Machine Learning Repository – Heart Disease Dataset](https://archive.ics.uci.edu/dataset/45/heart+disease)
* [Scikit-learn Documentation](https://scikit-learn.org/)
