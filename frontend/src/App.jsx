import { useState } from 'react'
import axios from 'axios'
import { motion } from 'framer-motion'
import './index.css'

function App() {
  const [inputText, setInputText] = useState('')
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleSubmit = async () => {
    if (!inputText.trim()) return;

    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await axios.post('http://localhost:8000/predict', { text: inputText });
      setResult(response.data);
    } catch (err) {
      console.error(err);
      setError(err.response?.data?.detail || err.message || "Failed to connect to backend");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="app-container">
      <header style={{ textAlign: 'center', marginBottom: '1rem' }}>
        <motion.h1
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
        >
          AegisMind
        </motion.h1>
        <p style={{ opacity: 0.8, fontSize: '1.2rem' }}>
          AI-Powered Suicide Ideation Detection & Prevention
        </p>
      </header>

      <div className="main-content">
        {/* Left Column: Analysiser Tool */}
        <motion.div 
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.8 }}
          className={`glass-container ${result?.prediction === 'Suicide' ? 'glow-red' : result?.prediction === 'Non-Suicide' ? 'glow-green' : ''}`}
        >
          <h2 style={{ marginTop: 0 }}>Analyze Text 🧠</h2>
          <p style={{ marginBottom: '1.5rem', opacity: 0.7 }}>
            Enter a message to analyze its sentiment and risk level using our Bidirectional LSTM model.
          </p>

          <textarea
            className="glass-input"
            placeholder="Type or paste text here (e.g., messages, notes, posts)..."
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
          />

          <button 
            className="glass-button"
            onClick={handleSubmit}
            disabled={loading || !inputText}
          >
            {loading ? 'Analyzing... 🔄' : 'Analyze Risk 🔍'}
          </button>

          {error && (
            <motion.div 
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              style={{ color: '#ff6b6b', marginTop: '1rem' }}
            >
              ⚠️ {error}
            </motion.div>
          )}

          {result && (
            <motion.div 
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: 1, scale: 1 }}
              className="stats-container"
            >
              <div className="stat-card">
                <h3>Prediction</h3>
                <h2 className={result.prediction === 'Suicide' ? 'result-suicide' : 'result-safe'}>
                  {result.prediction === 'Suicide' ? '🚨 Suicide' : '✅ Safe'}
                </h2>
              </div>
              <div className="stat-card">
                <h3>Confidence</h3>
                <h2>{(result.confidence * 100).toFixed(2)}%</h2>
              </div>
            </motion.div>
          )}
        </motion.div>

        {/* Right Column: Info & Stats */}
        <motion.div 
          initial={{ opacity: 0, x: 20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.8, delay: 0.2 }}
          className="info-section"
        >
          <div className="info-card mission-card">
            <h3>🛡️ Our Mission <span className="floating-icon">❤️</span></h3>
            <p>
              AegisMind utilizes advanced Natural Language Processing to detect early warning signs of suicide ideation in text. 
              Our goal is to assist mental health professionals and platforms in identifying individuals at risk.
            </p>
          </div>

          <div className="info-card">
            <h3>📊 Global Impact Stats</h3>
            <div className="stats-grid">
              <div className="stat-item">
                <span className="stat-number">703,000</span>
                <span className="stat-label">People die by suicide annually</span>
              </div>
              <div className="stat-item">
                <span className="stat-number">1 in 100</span>
                <span className="stat-label">Deaths worldwide is by suicide</span>
              </div>
              <div className="stat-item">
                <span className="stat-number">58%</span>
                <span className="stat-label">Occur before age 50</span>
              </div>
              <div className="stat-item">
                <span className="stat-number">2x</span>
                <span className="stat-label">Higher rate in males vs females</span>
              </div>
            </div>
            <p style={{marginTop: '1rem', fontSize: '0.8rem', opacity: 0.6}}>*Source: WHO 2019 Estimates</p>
          </div>

          <div className="info-card">
            <h3>🆘 Immediate Help</h3>
            <ul style={{ listStyleType: 'none', padding: 0 }}>
              <li style={{ marginBottom: '0.5rem' }}>📞 <strong>988</strong> - Suicide & Crisis Lifeline (USA)</li>
              <li style={{ marginBottom: '0.5rem' }}>📞 <strong>116 123</strong> - Samaritans (UK/ROI)</li>
              <li style={{ marginBottom: '0.5rem' }}>📞 <strong>91529 87821</strong> - iCall (India)</li>
              <li>💬 Text <strong>HOME</strong> to 741741</li>
            </ul>
             <div style={{ textAlign: 'center', marginTop: '1rem' }}>
                <span className="floating-icon" style={{ animationDelay: '0.5s' }}>🕊️</span>
                <span className="floating-icon" style={{ animationDelay: '1s', margin: '0 1rem' }}>🤝</span>
                <span className="floating-icon" style={{ animationDelay: '1.5s' }}>🌍</span>
             </div>
          </div>
        </motion.div>
      </div>
    </div>
  )
}

export default App
