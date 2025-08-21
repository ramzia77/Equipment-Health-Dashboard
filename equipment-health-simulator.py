import requests
import random
import time
from datetime import datetime

URL = "https://5ffe3b99103a.ngrok-free.app/webhook/tracker"  

# List of simulated construction equipment and locations
MACHINERY = [
    {"device_id": "EXC-01", "location": "Site A – Foundation Pit"},
    {"device_id": "CRN-02", "location": "Site B – Crane Bay"},
    {"device_id": "CEM-03", "location": "Site C – Concrete Zone"},
    {"device_id": "GEN-04", "location": "Site D – Power Hub"},
    {"device_id": "LFT-05", "location": "Tower 2 – Lift Shaft"},
    {"device_id": "MIX-06", "location": "Site A – Cement Mixer"},
]

while True:
    machinery = random.choice(MACHINERY)

    payload = {
        "device_id": machinery["device_id"],
        "temperature": round(random.uniform(30, 80), 2),  # e.g., engine or motor temperature
        "vibration": round(random.uniform(0, 100), 2),    # structural/motor vibrations
        "battery": round(random.uniform(10, 100), 2),     # power unit battery
        "location": machinery["location"],
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    try:
        res = requests.post(URL, json=payload)
        print(f"[{datetime.now()}] Sent: {payload} | Status: {res.status_code}")
    except Exception as e:
        print(f"❌ Error sending data: {e}")

    time.sleep(10)  # Send data every 10 seconds
