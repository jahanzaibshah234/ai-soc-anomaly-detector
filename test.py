import os
import pytest
from fastapi.testclient import TestClient
from main import app, CSV_FILE

@pytest.fixture(autouse=True)
def manage_csv_environment():
    """
    Automated MLOps Fixture: Backs up your real logs.csv file before tests run,
    creates a clean testing space, and restores your original file afterward.
    """
    backup_path = "logs_real_backup.csv"
    real_file_exists = os.path.exists(CSV_FILE)
    
    if real_file_exists:
        os.rename(CSV_FILE, backup_path)
        
    yield  # Runs tests
    
    if os.path.exists(CSV_FILE):
        os.remove(CSV_FILE)
        
    if real_file_exists:
        os.rename(backup_path, CSV_FILE)


# FIXTURE THAT EXPLICITLY RUNS STARTUP & LIFESPAN HOOKS
@pytest.fixture(scope="module", autouse=True)
def client():
    """Creates a test client that forces FastAPI to run its startup routines first"""
    # Using 'with' forces the application lifecycle state configuration to execute
    with TestClient(app) as test_client:
        yield test_client


# TEST 1: Verify the core Dashboard Web UI loads cleanly
def test_dashboard_ui_loading(client): 
    response = client.get("/")
    assert response.status_code == 200
    assert "AI Security Log Analyzer" in response.text


# TEST 2: Verify the AI Metrics JSON Aggregation route functions with clean states
def test_metrics_endpoint_aggregation(client): 
    response = client.get("/api/metrics")
    assert response.status_code == 200
    
    data = response.json()
    assert "risk_distribution" in data
    assert "failed_logins" in data
    assert "threat_trends" in data
    assert data["failed_logins"]["labels"] == ["No Data"]


# TEST 3: Verify the ML Model intercepts and flags Anomaly Attacks correctly
def test_ml_inference_catches_anomaly(client):
    malicious_payload = {
        "timestamp": "2026-05-30 02:30:00",
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
    
    response = client.post("/api/logs", json=malicious_payload)
    assert response.status_code == 200
    assert response.json()["result"] == "🚨 ANOMALY_DETECTED"
    assert os.path.exists(CSV_FILE)


# TEST 4: Verify the ML Model processes and accepts Standard Normal connections safely
def test_ml_inference_accepts_normal_traffic(client):
    normal_payload = {
        "timestamp": "2026-05-30 02:32:00",
        "ip": "192.168.1.25",
        "user": "user1",
        "event": "Web_Login",
        "status": "success",
        "attempts": 1,           
        "port": 443,
        "severity": "low",
        "user_agent": "Mozilla/5.0",
        "duration_ms": 30,
        "bytes_sent": 450,
        "country": "Local"
    }
    
    response = client.post("/api/logs", json=normal_payload)
    assert response.status_code == 200
    assert response.json()["result"] == "✅ NORMAL"