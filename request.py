import requests

# Pointing directly to your active FastAPI log processing endpoint
url = "http://127.0.0.1:8000/api/logs"

# Crafting a payload that your ML model will flag as a clear anomaly (15 attempts!)
payload = {
    "timestamp": "2026-05-25 02:49:00",
    "ip": "185.220.101.5",
    "user": "root",
    "event": "SSH_BRUTEFORCE",
    "status": "failed",
    "attempts": 15,
    "port": 22,
    "severity": "critical",
    "user_agent": "Hydra/v9.5",
    "duration_ms": 450,
    "bytes_sent": 2048,
    "country": "Russia"
}

response = requests.post(url, json=payload)
print("Server Response:", response.json())