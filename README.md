# 🛡️ Galaxy SMS Spam Filter

A live, production-ready Machine Learning web application that classifies SMS messages as **Spam 🚨** or **Safe (Ham) ✅** in real-time. Built with Python, Flask, Scikit-Learn, and Tailwind CSS, and deployed live on Render.

👉 **Live Application:** [https://galaxy-spam-filter.onrender.com/](https://galaxy-spam-filter.onrender.com/)

---

## ✨ Features

- **Real-Time Classification:** Instantly analyzes user-inputted text messages and predicts whether they are spam or safe.
- **Model Confidence Scores:** Displays real-time prediction confidence percentages calculated via Naive Bayes probability estimates (`predict_proba`).
- **Interactive Quick Samples:** Pre-loaded with 7 real-world test cases (spanning prize scams, banking/KYC alerts, credit card notices, and safe everyday messages) for instant testing.
- **Cosmic UI & UX:** Features a custom Tailwind CSS glassmorphism interface accompanied by a dynamic animated gradient background and twinkling star field.
- **Developer Convenience:** Supports keyboard shortcuts (`Enter` to submit quickly while keeping `Shift+Enter` for multi-line text).

---

## 🛠️ Tech Stack & Architecture

- **Backend:** Python, Flask, Gunicorn
- **Machine Learning:** Scikit-Learn (`MultinomialNB`, `CountVectorizer`, `train_test_split`)
- **Data Handling:** Pandas
- **Frontend:** HTML5, Tailwind CSS, Jinja2 Templates, Custom CSS Keyframes
- **Cloud Hosting:** Render (Cloud Platform)

---

## 📊 Dataset & Data Pipeline Rationale

- **Benchmark Dataset:** Trained on the benchmark **SMS Spam Collection Dataset**, originally created by researchers **Tiago A. Almeida** and **José María Gómez Hidalgo**, and hosted on the **UCI Machine Learning Repository**.
- **Data Acquisition Strategy:** Instead of fetching the compressed `.zip` archive directly from UCI (which introduces server-side decompression overhead and extra dependency requirements like `zipfile`/`io`), the application fetches a pre-formatted plain-text Tab-Separated Values (`.tsv`) file via a direct raw mirror:
  `https://raw.githubusercontent.com/justmarkham/DAT8/master/data/sms.tsv` (hosted by data science educator Kevin Markham).
- **Engineering Advantage:** This ensures lightweight, instantaneous server boots on cloud hosting platforms like Render without timeout risks or third-party storage redirects.

---

## 🚀 Project File Structure

```text
sms-spam-filter/
│
├── static/
│   └── logo.png          # Galaxy brand logo
├── templates/
│   └── index.html        # Main frontend UI (Tailwind CSS)
├── app.py                # Flask backend & ML model pipeline
├── Procfile              # Gunicorn process configuration for Render
└── requirements.txt      # Project Python dependencies
```
## ⚙️ Local Installation & Running Guide
If you want to run or test this project locally on your machine, follow these steps:

Clone the Repository:

Bash
git clone [https://github.com/VV-S70/sms-spam-filter.git](https://github.com/VV-S70/sms-spam-filter.git)
cd sms-spam-filter
Install Dependencies:

Bash
pip install -r requirements.txt
Run the Flask App:

Bash
python app.py
Open in Browser:
Navigate to http://127.0.0.1:5000/ in your web browser.

## 🛡️ License
This project is developed for academic presentation and machine learning demonstration purposes.
