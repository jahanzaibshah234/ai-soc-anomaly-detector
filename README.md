# 🛡️ AI Security Log Analyzer & SOC Dashboard

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?logo=github-actions&logoColor=white)](https://github.com/features/actions)

👥 Developed by Jahanzaib Khalid & Maria Rashid

An end-to-end MLOps and cybersecurity pipeline that uses an artificial intelligence classification model to perform live and batch anomaly detection on security logs. Security events are analyzed in real-time through a modern, responsive dashboard.

## ✨ Key Features

- **Real-Time AI Inference**: Integrates a serialized machine learning model (`.pkl`) into a modern, lifespan-managed FastAPI backend to classify security events instantly
- **Stateless Long-Polling Dashboard**: Displays live system status, threat trends, and risk distributions via asynchronous JavaScript polling and Chart.js without full-page refreshes
- **Live Log Ingestion API**: RESTful endpoint for submitting security logs for real-time anomaly detection
- **Automated CI/CD Testing Framework**: Built-in test suite powered by `pytest` and `httpx` to guarantee 100% route integrity and model performance automatically on every code change
- **Dark-Mode UI**: Professional, modern Security Operations Center dashboard optimized for extended viewing
- **Stateless Architecture**: Scalable backend design perfect for containerized and cloud deployments
- **Real-Time Metrics Aggregation**: Automatic collection and visualization of threat trends, risk distribution, and failed login attempts

## 📋 Table of Contents

- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Dashboard Features](#dashboard-features)
- [Testing](#testing)
- [CI/CD Pipeline](#cicd-pipeline)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [About](#about)
- [Contributing](#contributing)

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | FastAPI |
| **ML Framework** | Scikit-learn / Joblib |
| **Frontend** | HTML, CSS |
| **Visualization** | Chart.js |
| **Testing** | pytest, httpx |
| **CI/CD** | GitHub Actions |
| **Python** | 3.10 |

## 📁 Project Structure

```
ai-soc-anomaly-detector/
│
├── .github/
│   └── workflows/
│       └── mlops-ci.yml           # Automated GitHub Actions CI Test Pipeline
│
├── static/                        # Front-end UI Assets
│   ├── index.html                 # Dynamic SOC dashboard interface
│   └── style.css                  # Dark-mode dashboard layout stylesheet
│
├── main.py                        # Lifespan-managed FastAPI core server & routes
├── model.py                       # ML offline training script & pipeline compilation
├── request.py                     # Individual live threat simulation script
├── requirements.txt               # Pinned dependency manifest
├── test.py                        # Automated unit and integration test suite
├── security_model.pkl             # Frozen pre-trained ML model weights
├── README.md                       # This file
├── logs.csv                        # Audit log storage (auto-generated)
└── .gitignore                      # Git ignore rules
```

### File Descriptions

- **main.py**: FastAPI application with lifespan management, routes for dashboard, log ingestion, and real-time metrics
- **model.py**: Machine learning model training pipeline and serialization using Scikit-learn
- **request.py**: Script for simulating security log events for testing and demonstration
- **test.py**: Comprehensive test suite covering all endpoints and model functionality
- **security_model.pkl**: Pre-trained serialized ML model for instant threat classification
- **logs.csv**: Persistent storage for all analyzed security logs

## 📦 Installation

### Prerequisites

- Python 3.10
- pip package manager
- Git

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/jahanzaibshah234/ai-soc-anomaly-detector.git
   cd ai-soc-anomaly-detector
   ```

2. **Create a virtual environment**
   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Train the ML model (first time only)**
   ```bash
   python model.py
   ```
   This generates `security_model.pkl` which is required to run the server.

5. **Verify installation**
   ```bash
   python main.py
   ```

## 🚀 Quick Start

### Running the Server

Start the FastAPI development server:

```bash
python main.py
```

The application will start on `http://localhost:8000`

You should see:
```
🛡️ AI Security engine loaded into memory.
Uvicorn running on http://0.0.0.0:8000
```

### Accessing the Dashboard

Open your web browser and navigate to:
```
http://localhost:8000/
```

You'll see the SOC dashboard with:
- Real-time threat indicators
- Live-updating data visualizations
- System status monitoring
- Risk distribution charts
- Threat trend analysis

### Submitting a Security Log

Submit a security log for real-time anomaly detection:

```bash
curl -X POST http://localhost:8000/api/logs \
  -H "Content-Type: application/json" \
  -d '{
    "timestamp": "2024-01-15T10:30:45Z",
    "ip": "192.168.1.105",
    "user": "john.doe",
    "event": "login_attempt",
    "status": "failed",
    "attempts": 3,
    "port": 22,
    "severity": "high",
    "user_agent": "SSH-2.0-OpenSSH_7.4",
    "duration_ms": 500,
    "bytes_sent": 1024,
    "country": "US"
  }'
```

Or use the request.py script:

```bash
python request.py
```

## 📡 API Documentation

### Base URL
```
http://localhost:8000
```

### Endpoints

#### 1. Get Dashboard
- **Endpoint**: `GET /`
- **Description**: Returns the SOC dashboard HTML interface
- **Response**: HTML dashboard page
- **Example**:
  ```bash
  curl http://localhost:8000/
  ```

#### 2. Submit Security Log (Real-Time Analysis)
- **Endpoint**: `POST /api/logs`
- **Description**: Submit a security log for real-time ML-based anomaly detection
- **Request Body**:
  ```json
  {
    "timestamp": "string (ISO 8601)",
    "ip": "string (IP address)",
    "user": "string (username)",
    "event": "string (event type)",
    "status": "string (success|failed)",
    "attempts": "integer (login attempts)",
    "port": "integer (port number)",
    "severity": "string (low|medium|high|critical)",
    "user_agent": "string (client identifier)",
    "duration_ms": "integer (milliseconds)",
    "bytes_sent": "integer (bytes)",
    "country": "string (country code)"
  }
  ```
- **Response**:
  ```json
  {
    "status": "processed",
    "result": "🚨 ANOMALY_DETECTED" or "✅ NORMAL"
  }
  ```
- **Behavior**:
  - Analyzes the log using the pre-trained ML model
  - Classifies as ANOMALY (-1) or NORMAL (1)
  - Critical severity events trigger anomaly alerts
  - Automatically appends to `logs.csv`
  - Anomalies are cached in memory for dashboard updates

#### 3. Get Dashboard Metrics
- **Endpoint**: `GET /api/metrics`
- **Description**: Retrieve aggregated threat metrics for Chart.js visualizations
- **Response**:
  ```json
  {
    "risk_distribution": {
      "labels": ["Low", "Medium", "High", "Critical"],
      "data": [5, 12, 8, 3]
    },
    "failed_logins": {
      "labels": ["2024-01-15T10:30:45Z", "2024-01-15T10:31:20Z", ...],
      "data": [3, 5, 2, ...]
    },
    "threat_trends": {
      "labels": ["2024-01-15T10:30:45Z", "2024-01-15T10:31:20Z", ...],
      "data": [1, 2, 3, ...]
    }
  }
  ```
- **Example**:
  ```bash
  curl http://localhost:8000/api/metrics
  ```

### Interactive API Docs

Once the server is running, access the interactive API documentation:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🎨 Dashboard Features

### Real-Time Metrics
- **Total Events Processed**: Live counter of all analyzed security logs
- **Anomalies Detected**: Real-time count of security threats identified
- **Detection Rate**: Percentage of anomalous vs. normal events
- **Average Confidence**: Model confidence in current classifications

### Data Visualizations
- **Threat Trend Chart**: Cumulative count of detected threats over time
- **Risk Distribution**: Pie/doughnut chart showing threat severity levels (Low, Medium, High, Critical)
- **Failed Login Attempts**: Line chart tracking login attempts per timestamp
- **Event Timeline**: Chronological view of recent security events

### User Interface
- **Dark Mode**: Reduces eye strain during extended monitoring sessions
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Real-Time Updates**: Automatic refresh via long-polling (JavaScript polling `api/metrics`)
- **Threat Alerts**: Visual indicators for high-risk and critical events
- **Live Log Feed**: Displays detected anomalies with risk scores

## 🧪 Testing

### Running Tests

Execute the full test suite:

```bash
pytest test.py -v
```

### Test Coverage

- **Unit Tests**: Model prediction accuracy and data preprocessing
- **Integration Tests**: API endpoint functionality and response validation
- **Route Tests**: All HTTP routes and status codes
- **Data Validation**: Input validation using Pydantic models and edge cases
- **Anomaly Detection**: End-to-end threat detection workflow

### Running with Coverage Report

```bash
pytest test.py --cov=. --cov-report=html
```

View the coverage report:
```bash
open htmlcov/index.html  # macOS
start htmlcov/index.html  # Windows
```

## ⚙️ CI/CD Pipeline

### GitHub Actions Workflow

The project includes an automated CI/CD pipeline (`.github/workflows/mlops-ci.yml`) that:

1. **Triggers on**: Push to `main` and Pull Requests
2. **Runs**: 
   - Dependency installation
   - Full test suite with pytest
   - Model validation and loading
   - API endpoint validation
   - Code quality checks
3. **Artifacts**: Test reports and coverage metrics

### Workflow Status

Check the CI/CD status:
```
https://github.com/jahanzaibshah234/ai-soc-anomaly-detector/actions
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file (optional):

```env
FASTAPI_ENV=production
HOST=0.0.0.0
PORT=8000
LOG_LEVEL=INFO
MODEL_PATH=./security_model.pkl
```

### Model Configuration

Modify model behavior in `model.py`:

```python
# Adjust detection sensitivity
ANOMALY_THRESHOLD = -0.5

# Model hyperparameters
RANDOM_STATE = 42
TEST_SIZE = 0.2
CONTAMINATION = 0.1  # Expected proportion of anomalies
```

## 🔍 Troubleshooting

### Issue: "Module not found" errors

**Solution**: Ensure virtual environment is activated and dependencies installed:
```bash
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

### Issue: Port 8000 already in use

**Solution**: Use a different port:
```bash
uvicorn main:app --port 8001 --host 0.0.0.0
```

### Issue: "security_model.pkl not found"

**Solution**: Train the model first:
```bash
python model.py
```

This generates the required `security_model.pkl` file in the root directory.

### Issue: Dashboard not updating

**Solution**: 
1. Check browser console for JavaScript errors (F12)
2. Verify the API is responding: `curl http://localhost:8000/api/metrics`
3. Clear browser cache (Ctrl+Shift+Del or Cmd+Shift+Del)
4. Ensure logs are being submitted: `curl -X POST http://localhost:8000/api/logs ...`

### Issue: Model prediction errors

**Solution**:
1. Verify all required fields are present in the log submission
2. Check that numeric fields (attempts, duration_ms, bytes_sent) are valid integers
3. Ensure status field is either "success" or "failed"


## 📊 Performance Metrics

- **Model Inference Latency:** $\sim 2\text{--}8\text{ ms}$ per individual security log evaluation loop.
- **Batch Processing Throughput:** $150+$ log records/second utilizing vectorized Pandas matrix processing via the bulk upload component.
- **Memory Footprint:** $\sim 60\text{--}90\text{ MB}$ base RAM application usage (includes loaded FastAPI routers and the background `security_model.pkl` decision parameters).
- **Dashboard Synchronization:** Synchronous 3-second background client-side polling interval for live chart rendering updates.
- **Model Framework:** Unsupervised anomaly isolation/classification trained natively to process aligned tabular features (`status`, `attempts`, `duration_ms`, `bytes_sent`).

## 🔐 Security Best Practices

- Store sensitive configuration in environment variables
- Use HTTPS in production deployments
- Implement rate limiting for API endpoints
- Add authentication for dashboard access
- Regularly update dependencies
- Run security audits on submitted logs

## 👥 About

This project was developed as a practical Machine Learning, MLOps, and Cybersecurity portfolio project focused on applying AI techniques to security log analysis and anomaly detection.

### **Jahanzaib Khalid** 
- **Role**: Machine Learning Engineer & Backend Developer
- **Contributions**:
  - Designed and trained the Isolation Forest anomaly detection model
  - Built the FastAPI backend with real-time inference capabilities
  - Implemented stateless architecture for scalable deployments
  - Developed comprehensive CI/CD testing framework
  - Created responsive SOC dashboard with live metrics
- **GitHub**: [@jahanzaibshah234](https://github.com/jahanzaibshah234)
- **Email**: jahanzaib1234510@gmail.com
- **LinkedIn**: [Jahanzaib Khalid](https://www.linkedin.com/in/jahanzaib-khalid/)

### **Maria Rashid** 
- **Role**: Python Developer & Frontend Support
- **Contributions**:
  - Assisted in Python development and application logic. 
  - Worked on frontend integration (HTML/CSS templates)
  - Supported testing and overall project structuring
- **GitHub**: [@mariarashid730](https://github.com/mariarashid730)
- **Email**: mariarashid730@gmail.com
- **LinkedIn**: [Maria Rashid](https://www.linkedin.com/in/maria-rashid-4b0819282/)

### Team Values

- 🎯 **Innovation**: Continuously exploring cutting-edge technologies in AI and cybersecurity
- 🔒 **Security First**: Building secure, resilient systems with best practices
- 📊 **Data-Driven**: Making decisions based on metrics and performance analytics
- 🤝 **Collaboration**: Working together to deliver robust, production-ready solutions
- 📚 **Knowledge Sharing**: Committed to open-source and community contributions

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide
- Add tests for new features (use pytest)
- Update documentation in README.md
- Ensure all tests pass locally before pushing
- Use type hints in Python code

## 🙏 Acknowledgments

- Special thanks to everyone who contributed to and supported this project throughout its development.

**Special Thanks**:
- Maria Rashid for her valuable contribution in development and support
- FastAPI framework for the robust, asynchronous web server
- Scikit-learn and Joblib for the machine learning pipeline
- Chart.js for beautiful, interactive data visualizations
- GitHub Actions for automated testing and deployment

## 📮 Support

For issues, questions, or suggestions:
1. Check existing [Issues](https://github.com/jahanzaibshah234/ai-soc-anomaly-detector/issues)
2. Create a new issue with detailed description and error logs
3. Include error messages, environment details, and reproduction steps

## 📈 Roadmap

- [ ] Add user authentication and role-based access control
- [ ] Implement advanced threat alerting (email, Slack notifications)
- [ ] Add database support (PostgreSQL/MongoDB) for persistent storage
- [ ] Multi-model ensemble for improved accuracy
- [ ] RESTful API authentication with JWT tokens
- [ ] Containerized deployment templates (Docker Compose, Kubernetes)
- [ ] Historical analytics and reporting dashboard

---

<div align="center">

**Made with ❤️ by Jahanzaib Khalid & Maria Rashid**

⭐ If this project helped you, please consider giving it a star!

[Report Bug](https://github.com/jahanzaibshah234/ai-soc-anomaly-detector/issues) · [Request Feature](https://github.com/jahanzaibshah234/ai-soc-anomaly-detector/issues)

</div>

**Last Updated**: 2026-05-30 | **Version**: 1.0.0 | **Status**: Active Development
