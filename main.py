import os
import csv
import joblib
import pandas as pd
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from collections import Counter
from contextlib import asynccontextmanager

CSV_FILE = "logs.csv"
MODEL_FILE = "security_model.pkl"

# Global memory storage for runtime alerts so the dashboard loads instantly
detected_anomalies = []

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code here runs ON STARTUP (Before the server begins accepting requests)
    if not os.path.exists(MODEL_FILE):
        raise RuntimeError(f"⚠️ {MODEL_FILE} not found! Run model.py first.")
    
    app.state.model = joblib.load(MODEL_FILE)
    print("🛡️ AI Security engine loaded into memory.")
    
    yield # ──> The application runs while hooked here
    
    # Any code placed here will run ON SHUTDOWN (When you stop the server)
    print("🛑 AI Security engine shutting down cleanly.")

# 3. Pass the lifespan manager directly into your FastAPI app instance initialization
app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="static")

# Pydantic Data Validator for incoming logs
class SecurityLog(BaseModel):
   timestamp: str
   ip: str
   user: str
   event: str
   status: str
   attempts: int
   port: int
   severity: str
   user_agent: str
   duration_ms: int
   bytes_sent: int
   country: str   

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
   return templates.TemplateResponse(
      request=request,
      name="index.html",
      context={"threats": detected_anomalies[::-1]}
   )
    
@app.post("/api/logs")
async def collect_and_analyze_log(log: SecurityLog):

   # Convert incoming object to a dictionary
   log_dict = log.model_dump()

   # Extract and format values for the ML model
   status = 0 if log_dict['status'] == 'success' else 1
   input_data = pd.DataFrame([{
      'status': status,
      'attempts': log_dict['attempts'],
      'duration_ms': log_dict['duration_ms'],
      'bytes_sent': log_dict['bytes_sent']
   }])

   # Use the pre-loaded model to predict instantly (-1 = Anomaly, 1 = Normal)
   prediction = app.state.model.predict(input_data)[0]

   # Save the log by automatically appending it to your CSV sheet
   file_exists = os.path.exists(CSV_FILE)
   with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as f:
      writer = csv.DictWriter(f, fieldnames=log_dict.keys())
      if not file_exists:
         writer.writeheader()
      writer.writerow(log_dict)

   # If marked as anomaly, calculate risk score and push to the live alerts feed
   if prediction == -1 or log_dict.get("severity") == "critical":
      log_dict["risk_score"] = min(log_dict['attempts'] * 10, 100)
      detected_anomalies.append(log_dict)
      return {"status": "processed", "result": "🚨 ANOMALY_DETECTED"}
   
   return {"status": "processed", "result": "✅ NORMAL"}

# NEW AGGREGATION ENDPOINT FOR YOUR CHART.JS DASHBOARD
@app.get("/api/metrics")
async def get_dashboard_metrics():
   """
   Parses live anomalies inside memory or the logs.csv file
   and aggregates them down into arrays tailored directly for Chart.js.
   """

   # Counts frequencies of low, medium, high, critical via log metrics
   severity_list = [log["severity"].capitalize() for log in detected_anomalies]
   severity_counts = Counter(severity_list)
    
   risk_distribution = {
      "labels": ["Low", "Medium", "High", "Critical"],
      "data": [
         severity_counts.get("Low", 0),
         severity_counts.get("Medium", 0),
         severity_counts.get("High", 0),
         severity_counts.get("Critical", 0)
      ]
   }


   # Grabs the last 7 logged events timestamps and values
   recent_logs = detected_anomalies[-7:]

   failed_logins = {
      "labels": [log["timestamp"] for log in recent_logs] if recent_logs else ["No Data"],
      "data": [log["attempts"] for log in recent_logs] if recent_logs else [0]
   }

   # Generates a progressive accumulation scale of threats caught over time
   trend_labels = []
   trend_data = []
   cumulative_count = 0

   for log in recent_logs:
      cumulative_count += 1
      trend_labels.append(log["timestamp"])
      trend_data.append(cumulative_count)

   threat_trends = {
      "labels": trend_labels if trend_labels else ["No Data"],
      "data": trend_data if trend_data else [0]
   }

   return {
      "risk_distribution": risk_distribution,
      "failed_logins": failed_logins,
      "threat_trends": threat_trends
   }
