# 🖊️ Digit Recognizer Web App

🔗 **Live Demo:** [digit-recognize.onrender.com](https://digit-recognize.onrender.com)

![Demo GIF](DEMO.gif)

A **Flask-based web application** that serves a **machine learning model** for **digit recognition**.
Configured for **production deployment** on **Render** with **Gunicorn**.
 
---

## ⚙️ Technologies

- **Backend:** Flask
- **Machine Learning:** TensorFlow
- **WSGI Server:** Gunicorn
- **Database Connector:** Psycopg2
- **Core Libraries:** NumPy, Matplotlib

---

## 📂 Project Structure

```
digit_recognize/
├── app.py              # Main Flask app
├── requirements.txt    # pip dependencies
├── render.yaml         # Render deployment config
├── environment.yml     # (Optional) Conda env file
├── run.sh              # Local dev setup script
└── README.md           # Project documentation
```

---

## 🚀 Running Locally

This project uses **uv** (fast Python installer), but works with any virtual environment.

1. **Clone the repository**

```bash
git clone https://github.com/ankitsharma-tech/Digit-Recognize.git
cd Digit-Recognize
```

2. **Create & activate a virtual environment**

```bash
# For Python 3.8
python3.8 -m venv .venv
source .venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Start the app**

```bash
python app.py
```

App will be available at 👉 `http://0.0.0.0:5000`

---

## ☁️ Deployment on Render

This app is **deployment-ready** with `render.yaml`.

1. Push code to GitHub / GitLab / Bitbucket
2. In **Render Dashboard** → click **“New +” → “Web Service”**
3. Connect your repo
4. Render auto-detects `render.yaml` and applies:

   - **Python:** `3.8.10`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`

5. Click **“Create Web Service”** → live URL provided on success 🚀

---
