# 🤖 Wrist Flexion Detection - ML Model

This is a part of our **Biomedical Device Design** project. It includes a machine learning pipeline to classify wrist flexion based on biosignal input.

---

## 🧩 Overview

This includes:

- Training a **Random Forest Classifier** using handcrafted features
- Real-time signal classification via **Streamlit** app
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

These features are passed to the Random Forest model for classification.

---

