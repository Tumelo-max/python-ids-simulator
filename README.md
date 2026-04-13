# 🚨 Python Intrusion Detection System (IDS)

## 📌 Overview
This project is a Python-based Intrusion Detection System that monitors network traffic and detects suspicious activity based on repeated connection attempts.

## ⚙️ Features
- Detects repeated IP connections
- Flags suspicious behavior
- Logs alerts to a file
- Real-time monitoring output

## 🧠 How It Works
The system tracks IP addresses and counts how many requests they make within a short time window. If a threshold is exceeded, it raises an alert.

## 🚀 How to Run
```bash
python3 ids.py
