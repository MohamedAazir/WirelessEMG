# 🤖 Wrist Flexion Detection - ML Model

This is a part of our **Biomedical Device Design** project. It includes a machine learning pipeline to classify wrist flexion based on biosignal input.

---

## 🧩 Overview

This includes:

- Training a **Random Forest Classifier** using handcrafted features
- signal classification display via **Streamlit** app
- A lightweight CLI tool for batch or test use

---

## 📁 Files in This Folder

| File                         | Description                                               |
|------------------------------|-----------------------------------------------------------|
| `random_forest_updated.py`   | Trains the model and saves it as `.joblib`               |
| `app_updated.py`             | Streamlit-based app for uploading and classifying signals|
| `real_time_clf.py`           | CLI tool for running classification from CSV input       |
| `random_forest_updated_model.joblib` | Trained model file (generated after training) |

---

## 📊 Features Used for Classification

From each `Amplitude` signal, we extract **7 statistical features**:

- Mean
- Standard Deviation
- Maximum
- Minimum
- Range
- Median
- Root Mean Square (RMS)


<p align="center">
  <img src="https://github.com/user-attachments/assets/2c370d9e-d4b6-48f1-aeaf-942feaee3b40" width="50%"/>
</p>


These features are passed to the Random Forest model for classification.


## 📊 Model Evaluation

<p align="center">
  <img src="https://github.com/user-attachments/assets/87a36ac4-9303-4d23-a760-65dc998abe31" width="50%" />
</p>


---

## 🖼️ App Preview

<p align="center">
  <img src="https://github.com/user-attachments/assets/73278f74-fe3f-4204-9054-22b7fb15cedb" width="45%" style="margin-right: 10px;" />
  <img src="https://github.com/user-attachments/assets/734a708f-9f72-4f5d-b03c-f345c0d32f4e" width="49%" />
</p>


