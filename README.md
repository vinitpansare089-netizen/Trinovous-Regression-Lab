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

|Random Forest Regressor (tuned)

|### Performance

| Metric | Value |
|-------|------|
| Train RMSE | ~2.37 |
| Test RMSE | ~3.97 |
| MAE | ~3.22 |
| R² Score | ~0.23|


Two modeling approaches:

1. Without prior grades → realistic scenario (RMSE ~4)
2. With G2 included → high accuracy scenario (RMSE ~2)
---

## 📊 Model Evaluation

### Problem Type
This is a regression problem (predicting continuous student scores).

### Metrics Used
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)
- R² Score

### Model Comparison

| Model | Train RMSE | Test RMSE | Observation |
|------|-----------|----------|-------------|
| Linear Regression | ~3.8 | ~4.2 | Stable but less accurate |
| Decision Tree | 0.0 | ~4.7 | Overfitting |
| Random Forest (unrestricted) | ~1.4 | ~3.96 | Overfitting |
| Random Forest (tuned) | ~2.37 | ~3.97 | Best balance |

### Final Model
Random Forest Regressor (tuned)

### Why this model?
-### Interpretation
- Model predictions are on average off by ~3–4 marks
- Shows moderate predictive power due to limited features
- Demonstrates reasonable generalization without severe overfitting

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

npm start (frontend)
uvicorn app:app --reload
