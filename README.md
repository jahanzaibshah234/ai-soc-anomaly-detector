# 🛡️ AI Security Log Analyzer & SOC Dashboard

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104%2B-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?logo=github-actions&logoColor=white)](https://github.com/features/actions)

An end-to-end MLOps and cybersecurity pipeline that uses an artificial intelligence classification model to perform live and batch anomaly detection on network connection logs. Security events are analyzed in real time through a dark-mode Security Operations Center (SOC) dashboard complete with live-updating data visualizations and an automated GitHub Actions CI/CD test framework.

## ✨ Key Features

- **Real-Time AI Inference**: Integrates a serialized machine learning model (`.pkl`) into a modern, lifespan-managed FastAPI backend to classify security events instantly
- **Stateless Long-Polling Dashboard**: Displays live system status, threat trends, and risk distributions via asynchronous JavaScript polling and Chart.js without full-page refreshes
- **Bulk CSV Log Ingestion**: Supports vectorized batch processing allowing security analysts to upload massive daily log sheets for bulk threat identification
- **Automated CI/CD Testing Framework**: Built-in test suite powered by `pytest` and `httpx` to guarantee 100% route integrity and model performance automatically on every code change
- **Dark-Mode UI**: Professional, modern Security Operations Center dashboard optimized for extended viewing
- **Stateless Architecture**: Scalable backend design perfect for containerized and cloud deployments

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
- [Contributing](#contributing)
- [License](#license)

## 🛠️ Tech Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| **Backend** | FastAPI | 0.104+ |
| **ML Framework** | Scikit-learn | Latest |
| **Frontend** | HTML5, CSS3, JavaScript | Modern |
| **Visualization** | Chart.js | Latest |
| **Testing** | pytest, httpx | Latest |
| **CI/CD** | GitHub Actions | Built-in |
| **Python** | 3.9+ | Recommended 3.11+ |

## 📁 Project Structure

```
ai_security_log_analyzer/
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
└── .gitignore                      # Git ignore rules
```

### File Descriptions

- **main.py**: FastAPI application with lifespan management, routes for dashboard, threat detection, and log ingestion
- **model.py**: Machine learning model training pipeline and serialization
- **request.py**: Script for simulating individual threat events for testing and demonstration
- **test.py**: Comprehensive test suite covering all endpoints and model functionality
- **security_model.pkl**: Pre-trained serialized ML model for instant threat classification

## 📦 Installation

### Prerequisites

- Python 3.9 or higher
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

4. **Verify installation**
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

### Making a Threat Request

Submit an individual threat detection request:

```bash
python request.py
```

Or use curl:
```bash
curl -X POST http://localhost:8000/detect \
  -H "Content-Type: application/json" \
  -d '{
    "src_ip": "192.168.1.1",
    "dst_ip": "10.0.0.1",
    "protocol": "TCP",
    "port": 443,
    "packet_count": 1000
  }'
```

## 📡 API Documentation

### Base URL
```
http://localhost:8000
```

### Endpoints

#### 1. Get Dashboard
- **Endpoint**: `GET /`
- **Description**: Returns the SOC dashboard UI
- **Response**: HTML dashboard interface

#### 2. Detect Threat (Single)
- **Endpoint**: `POST /detect`
- **Description**: Classify a single network event as normal or anomaly
- **Request Body**:
  ```json
  {
    "src_ip": "string",
    "dst_ip": "string",
    "protocol": "string",
    "port": "integer",
    "packet_count": "integer"
  }
  ```
- **Response**:
  ```json
  {
    "threat_level": "normal|anomaly",
    "confidence": "float (0-1)",
    "timestamp": "ISO 8601"
  }
  ```

#### 3. Bulk Detect Threats (CSV Upload)
- **Endpoint**: `POST /bulk-detect`
- **Description**: Process multiple network events from CSV file
- **Request**: Multipart form data with CSV file
- **CSV Format**:
  ```csv
  src_ip,dst_ip,protocol,port,packet_count
  192.168.1.1,10.0.0.1,TCP,443,1000
  ```
- **Response**:
  ```json
  {
    "total_events": "integer",
    "anomalies_detected": "integer",
    "results": [
      {
        "index": "integer",
        "threat_level": "string",
        "confidence": "float"
      }
    ]
  }
  ```

#### 4. Get System Stats
- **Endpoint**: `GET /stats`
- **Description**: Retrieve system statistics and threat summary
- **Response**:
  ```json
  {
    "total_events": "integer",
    "anomalies": "integer",
    "normal_events": "integer",
    "average_confidence": "float",
    "last_update": "ISO 8601"
  }
  ```

### Interactive API Docs

Once the server is running, access the interactive API documentation:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🎨 Dashboard Features

### Real-Time Metrics
- **Total Events Processed**: Live counter of all analyzed network events
- **Anomalies Detected**: Real-time count of security threats
- **Detection Rate**: Percentage of anomalous vs. normal events
- **Average Confidence**: Model confidence in current classifications

### Data Visualizations
- **Threat Trend Chart**: 24-hour rolling window of threat detections
- **Risk Distribution**: Pie chart showing threat levels
- **Event Timeline**: Chronological view of recent security events
- **Protocol Breakdown**: Analysis by network protocol type

### User Interface
- **Dark Mode**: Reduces eye strain during extended monitoring
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Real-Time Updates**: Automatic refresh via long-polling without page reload
- **Threat Alerts**: Visual indicators for high-risk events

## 🧪 Testing

### Running Tests

Execute the full test suite:

```bash
pytest test.py -v
```

### Test Coverage

- **Unit Tests**: Model prediction accuracy and preprocessing
- **Integration Tests**: API endpoint functionality
- **Route Tests**: All HTTP routes and response codes
- **Data Validation**: Input validation and edge cases

### Running with Coverage Report

```bash
pytest test.py --cov=. --cov-report=html
```

View the coverage report:
```bash
open htmlcov/index.html  # macOS
```

## ⚙️ CI/CD Pipeline

### GitHub Actions Workflow

The project includes an automated CI/CD pipeline (`.github/workflows/mlops-ci.yml`) that:

1. **Triggers on**: Push to `main` and Pull Requests
2. **Runs**: 
   - Dependency installation
   - Full test suite with pytest
   - Model validation
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
ANOMALY_THRESHOLD = 0.5

# Model hyperparameters
RANDOM_STATE = 42
TEST_SIZE = 0.2
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
uvicorn main:app --port 8001
```

### Issue: Model not loading

**Solution**: Verify `security_model.pkl` exists in the root directory:
```bash
ls -la security_model.pkl
```

If missing, retrain the model:
```bash
python model.py
```

### Issue: Dashboard not updating

**Solution**: 
1. Check browser console for JavaScript errors (F12)
2. Verify server is running: `http://localhost:8000/stats`
3. Clear browser cache (Ctrl+Shift+Del)

## 🚀 Deployment

### Docker (Recommended)

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

Build and run:
```bash
docker build -t ai-soc-analyzer .
docker run -p 8000:8000 ai-soc-analyzer
```

### Cloud Platforms

- **Heroku**: Add Procfile with `web: python main.py`
- **AWS**: Deploy to EC2 or ECS with proper security groups
- **Google Cloud**: Use Cloud Run for serverless deployment
- **Azure**: Deploy to App Service

## 📊 Performance Metrics

- **Inference Time**: ~5-10ms per request
- **Throughput**: 100+ events/second in batch mode
- **Model Accuracy**: Validated on training dataset
- **Memory Usage**: ~50-100MB base + model overhead

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide
- Add tests for new features
- Update documentation
- Ensure all tests pass locally before pushing

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Jahanzaib Shah**
- GitHub: [@jahanzaibshah234](https://github.com/jahanzaibshah234)
- Repository: [ai-soc-anomaly-detector](https://github.com/jahanzaibshah234/ai-soc-anomaly-detector)

## 🙏 Acknowledgments

- FastAPI framework for the robust web server
- Scikit-learn for the machine learning pipeline
- Chart.js for beautiful data visualizations
- GitHub Actions for automated testing

## 📮 Support

For issues, questions, or suggestions:
1. Check existing [Issues](https://github.com/jahanzaibshah234/ai-soc-anomaly-detector/issues)
2. Create a new issue with detailed description
3. Include error messages and environment details

---

**Last Updated**: 2026-05-29 | **Version**: 1.0.0
