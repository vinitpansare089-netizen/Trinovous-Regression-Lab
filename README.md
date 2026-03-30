# 🎓 Student Performance Prediction (Trinovous)

## 🚀 Overview
This project predicts student final grades (G3) using machine learning.

Built as part of my AI/ML journey under the **Trinovous** brand.

---

## 🧠 Problem Statement
Predict student performance based on behavioral and academic features.

---

## ⚙️ Features
- Data preprocessing (encoding, scaling)
- Feature selection (removed G1, G2 to avoid leakage)
- Model training with hyperparameter tuning (GridSearchCV)
- Evaluation using RMSE
- Prediction pipeline for new data
- Logging & experiment tracking

---

## 📊 Model Performance

| Metric | Value |
|-------|------|
| Train RMSE | ~3.7 |
| Test RMSE | ~4.4 |

---

## 🧪 Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn

---

## 📁 Project Structure

project/
├── src/
├── models/
├── artifacts/
├── data/
├── main.py


---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python main.py