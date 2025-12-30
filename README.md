# 🛡️ AegisMind
### AI-Powered Suicide Risk Detection Platform

---

## 📌 Overview

**AegisMind** is an end-to-end Deep Learning–based mental health safety system designed to detect **suicidal ideation** from user-generated text.  
The system analyzes messages in real time and classifies them into risk levels, enabling early intervention through responsible AI practices.

This project follows **production-level engineering standards**, including modular code design, API-based inference, frontend integration, logging, exception handling, and MLOps readiness.

---

## 🎯 Problem Statement

Suicidal thoughts are often expressed subtly in text messages, chats, or online posts.  
Manual detection is slow, subjective, and impossible to scale.

**AegisMind** addresses this challenge by:
- Automatically analyzing text data
- Detecting high-risk suicidal intent with a focus on recall
- Providing real-time predictions via an API and web interface

---

## 🚀 Key Features

- 🧠 Deep Learning–based NLP model for suicide risk detection  
- ⚡ Real-time inference using FastAPI  
- 🌐 Interactive Streamlit frontend  
- 📊 Risk-level classification with confidence scores  
- 🧪 Evaluation using Recall, Precision, and F1-score  
- ⚙️ MLOps-ready architecture (Docker, DVC, CI/CD)  
- 🧾 Centralized logging and custom exception handling  

---

## 🧠 Model Details

- **Model Type:** BiLSTM (Binary Text Classification)
- **Input:** User text message
- **Output:** Suicide risk probability
- **Loss Function:** Binary Crossentropy
- **Primary Metric:** Recall  
- **Secondary Metrics:** Precision, F1-score

> Recall is prioritized to minimize false negatives, as missing a high-risk case is more critical than raising a false alarm.

---

## 🛠️ Tech Stack

### Machine Learning
- Python
- TensorFlow / Keras
- NLP (Tokenization, Padding, Embeddings)

### Backend
- FastAPI
- Pydantic

### Frontend
- Javascript(React)

### MLOps
- Docker
- DVC

### Utilities
- Custom Exception Handling
- Centralized Logging




