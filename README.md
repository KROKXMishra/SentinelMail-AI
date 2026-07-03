# SentinelMail AI

An AI-powered Spam & Phishing Detection Platform built using **Flask**, **Machine Learning**, **MySQL**, and **Docker**. SentinelMail AI helps users detect spam or phishing messages, view prediction history, generate PDF reports, and monitor statistics through an interactive dashboard.

---

## Features

- User Registration & Login Authentication
- Spam/Ham Detection using Machine Learning
- Confidence Score for Every Prediction
- Risk Level Classification
- Interactive Dashboard
- Prediction History
- Delete Individual Prediction
- Delete Complete History
- PDF Report Generation
- Docker Support
- Responsive UI

---

## Tech Stack

### Backend

- Flask
- Flask-Login
- Flask-Bcrypt
- Flask-WTF
- SQLAlchemy

### Machine Learning

- Scikit-Learn
- TF-IDF Vectorizer
- Multinomial Naive Bayes
- NLTK

### Database

- MySQL

### Report Generation

- ReportLab

### Containerization

- Docker
- Docker Compose

---

## Project Structure

```
SentinelMail-AI
│
├── forms/                  # Login & Registration Forms
├── models/                 # SQLAlchemy Models
├── notebooks/              # Model Training Notebook
├── reports/                # Generated PDF Reports
├── routes/                 # Flask Blueprints
│   ├── auth.py
│   ├── dashboard.py
│   ├── history.py
│   ├── predict.py
│   └── report.py
│
├── services/
│   ├── llm/                # LLM Services
│   ├── ml/                 # ML Prediction Logic
│   └── pdf/                # PDF Generator
│
├── static/                 # CSS & Static Files
├── templates/              # HTML Templates
│
├── app.py
├── run.py
├── config.py
├── extensions.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .dockerignore
└── README.md
```

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/SentinelMail-AI.git

cd SentinelMail-AI
```

---

### 2. Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file in the project root.

```env
SECRET_KEY=your_secret_key

DB_HOST=localhost
DB_PORT=3306
DB_NAME=sentinelmail
DB_USER=root
DB_PASSWORD=your_password

GROQ_API_KEY=your_groq_api_key
```

---

### 5. Run the Application

```bash
python run.py
```

Visit

```
http://127.0.0.1:5000
```

---

# Running with Docker

### Build Image

```bash
docker compose build
```

### Start Container

```bash
docker compose up
```

### Run in Background

```bash
docker compose up -d
```

### Stop Container

```bash
docker compose down
```

Application URL

```
http://localhost:5000
```

---

# Screenshots

Add screenshots of:

- Home Page
- Registration Page
- Login Page
- Dashboard
- Prediction Page
- History Page
- PDF Report

---

## Future Improvements

- URL Reputation Analysis
- Email Header Analysis
- Explainable AI for Predictions
- Email Attachment Scanning
- Real-time Spam Detection API
- Cloud Deployment (AWS / Azure / GCP)
- Admin Dashboard
- Dark/Light Theme Toggle

---

## Author

**Kallol Mishra**

B.Tech Computer Science & Engineering

National Institute of Technology Durgapur

GitHub: https://github.com/<your-github-username>

---

## License

This project is developed for educational and learning purposes.