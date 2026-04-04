# 🎓 Student Performance Prediction (Trinovous)

## 🔥 Key Highlights
- Built a complete ML pipeline from scratch
- Implemented data preprocessing & feature engineering
- Performed hyperparameter tuning using GridSearchCV
- Achieved stable model performance with proper evaluation
- Designed prediction system for real-world usage

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

|Random Forest 

| Metric | Value |
|-------|------|
| Train RMSE | ~1.48 |
| Test RMSE | ~3.96 |

Two modeling approaches:

1. Without prior grades → realistic scenario (RMSE ~4)
2. With G2 included → high accuracy scenario (RMSE ~2)
---

## 🧪 Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- React
- Express(server)
- FastAPI

---

## 📁 Project Structure

project/
├── src/
├── models/
├── artifacts/
├── data/
├── main.py

later: frontend and backend
and fine tuning model again
for better model predictions
currently not satisfied with result.


---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python main.py
