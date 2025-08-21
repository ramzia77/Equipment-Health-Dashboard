# ⚙️ Equipment Health Tracker

[![GitHub stars](https://img.shields.io/github/stars/yourusername/yourrepo?style=social)][(https://github.com/ramzia77))]

[![Maintenance](https://img.shields.io/badge/Maintained-Yes-green)](https://github.com/yourusername/yourrepo)

> 🔥 Real-time construction equipment monitoring with simulated IoT data, alerts, and live dashboard. Fully IoT-ready and ERP/CMMS integration capable.

---

## 🚀 Project Overview  

Welcome to **Equipment Health Tracker** – the future of **smart construction equipment monitoring**!  

- Monitors **temperature 🌡️**, **battery ⚡**, and **vibration 🌀**.  
- Simulated data shows live alerts and trends.  
- Fully React + Firebase dashboard for real-time visualization.  
- Alert delivery via **Email 📧**, **Slack 💬**, and **Trello 📋**.

![Dashboard GIF](https://media.giphy.com/media/yourdemo.gif)

---

## 🎯 Business Value  

- **Preventive maintenance** → reduce downtime  
- **Safety enhancement** → detect anomalies early  
- **Operational efficiency** → optimize equipment usage  
- **ERP/CMMS Integration-ready** → seamless workflow sync  

---

## ✨ Features  

- **🚀 Real-time Monitoring:** Live React dashboard via Firebase  
- **⚡ Alerts System:** Email, Slack, Trello notifications  
- **📊 Trends Visualization:** Line charts for temperature, battery, vibration  
- **🖥 Simulated IoT Devices:** Python simulator (`equipment-health-simulator.py`)  
- **💾 Data Storage:** Firebase for persistent real-time data  
- **🛠 Tooling:** TailwindCSS, Vite, ESLint, PostCSS  

---

## 🏗 Architecture  

```mermaid
graph LR
A[Simulated Devices] --> B[Python Simulator]
B --> C[n8n Webhook Workflow]
C --> D[Alert Delivery]
C --> E[Firebase]
E --> F[React Dashboard]
D --> G[Email / Slack / Trello]
