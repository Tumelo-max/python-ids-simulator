# 🛡️ Python IDS Simulator

A lightweight Intrusion Detection System (IDS) built in Python that simulates network monitoring and detects suspicious IP activity based on connection thresholds.

---

## 🚀 Overview

This project demonstrates how basic intrusion detection logic works by tracking repeated IP connections and flagging abnormal behavior.

It is designed as a foundational cybersecurity project to simulate how Security Operations Centers (SOC) detect suspicious traffic patterns.

---

## ⚙️ Features

- Tracks incoming IP addresses
- Counts repeated connections per IP
- Detects suspicious activity using threshold-based logic
- Logs alerts to a file (`ids_log.txt`)
- Simple command-line interface for testing

---

## 🧠 How It Works

If an IP address exceeds a defined threshold (5 requests), it is flagged as suspicious:
