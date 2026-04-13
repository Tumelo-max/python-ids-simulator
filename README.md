# 🛡️ Python IDS Simulator

A simple Intrusion Detection System (IDS) simulator built in Python that monitors incoming IP traffic and detects suspicious behavior based on request frequency.

---

## 🚀 Features

- Real-time IP monitoring
- Detection levels:
  - NORMAL
  - MEDIUM (unusual activity)
  - HIGH (suspicious activity / possible attack)
- Time-based traffic analysis (sliding window)
- Cooldown system to prevent alert spam
- Event logging to file (`ids_log.txt`)

---

## 🧠 How It Works

The system tracks how many requests an IP makes within a short time window:

- If requests exceed a threshold → HIGH alert
- If approaching threshold → MEDIUM alert
- Otherwise → NORMAL traffic

---

## ⚙️ Configuration

```python
THRESHOLD = 5
TIME_WINDOW = 10
COOLDOWN = 15
