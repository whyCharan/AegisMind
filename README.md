# 🛡️ AegisMind
### AI-Powered Suicide Risk Detection Platform

---

## 📌 Overview

**AegisMind** is an advanced AI system designed to detect **suicidal ideation** in text. Utilizing a **Bidirectional LSTM** deep learning model, it analyzes emotional patterns and context to identify high-risk messages in real-time.

The project features a **premium Glassmorphism UI** built with **React & Vite**, offering a seamless and modern user experience while communicating with a robust **FastAPI** backend.

---

## 🚀 Key Features

- **🧠 Advanced NLP Model**: Bidirectional LSTM trained for high recall and precision on suicide detection datasets.
- **⚡ Real-time Analysis**: Instant classification via FastAPI endpoints.
- **🎨 Modern UI**: Stunning **Glassmorphism** design with smooth animations and dynamic gradients.
- **📊 Live Statistics**: Immediate visualization of prediction results and confidence scores.
- **🛠️ Production Ready**: Modular component design, exception handling, and easy deployment scripts.

---

## 🛠️ Tech Stack

### Frontend
- **React 18**
- **Vite**
- **CSS3 (Glassmorphism & Animations)**
- **Axios & Framer Motion**

### Backend
- **Python 3.8+**
- **FastAPI** (REST API)
- **TensorFlow / Keras** (Deep Learning)
- **NLTK** (Text Preprocessing)

---

## 📦 Installation & Usage

### One-Click Start (Windows)
Simply run the included batch file to install dependencies, train the model, and launch the application:
```bash
run.bat
```

### Manual Setup

1. **Backend Setup**
   ```bash
   pip install -r requirements.txt
   python components/train.py   # Train the model
   uvicorn api.main:app --reload # Start API server
   ```

2. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

3. **Access**
   Open your browser to `http://localhost:5173`.

---

## 🧠 Model Architecture

The core of AegisMind is a **Bidirectional Long Short-Term Memory (Bi-LSTM)** network.
- **Embedding Layer**: Learnable vector representations of words.
- **Bi-LSTM Layers**: Captures context from both past and future words in the sequence.
- **Dense Layers**: Fully connected layers with dropout for regularization.
- **Sigmoid Output**: Probability score (0-1) for binary classification.

