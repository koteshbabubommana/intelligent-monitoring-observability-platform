# Intelligent Monitoring & Observability Platform

A backend monitoring platform for tracking API health, request metrics, latency signals, and anomaly patterns using FastAPI, Prometheus metrics, and machine learning based anomaly detection.

## Architecture

```text
Client / API User
        ↓
FastAPI Backend
        ↓
Monitoring APIs
        ↓
Prometheus Metrics Endpoint
        ↓
Anomaly Detection Engine
        ↓
Structured Logs + API Response
```

## Tech Stack

- Python
- FastAPI
- Prometheus Client
- Scikit-learn
- NumPy
- Docker
- Docker Compose
- Pytest

## Features

- REST API monitoring endpoints
- Health check API
- Prometheus-compatible metrics endpoint
- API request tracking
- Latency and error-based anomaly detection
- ML-based anomaly detection using Isolation Forest
- Structured logging
- Dockerized backend setup
- Swagger API documentation
- Unit test support

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Home endpoint |
| GET | `/health` | Health check endpoint |
| GET | `/detect-anomaly` | Detect abnormal latency/error/request patterns |
| GET | `/metrics` | Prometheus metrics endpoint |

## Run Instructions

### 1. Clone the repository

```bash
git clone https://github.com/koteshbabubommana/intelligent-monitoring-observability-platform.git
cd intelligent-monitoring-observability-platform
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the API locally

```bash
python -m uvicorn app.main:app --reload
```

### 4. Open Swagger API Docs

```text
http://127.0.0.1:8000/docs
```

### 5. Test anomaly detection

Use:

```text
GET /detect-anomaly
```

Sample parameters:

```text
latency_ms = 900
error_count = 12
request_count = 500
```

Sample response:

```json
{
  "latency_ms": 900.0,
  "error_count": 12,
  "request_count": 500,
  "anomaly_score": -0.24499506985299802,
  "is_anomaly": true
}
```

### 6. Run with Docker

```bash
docker compose up --build
```

## Project Structure

```text
intelligent-monitoring-observability-platform/
├── app/
│   ├── api/
│   │   ├── ml/
│   │   │   └── anomaly_detector.py
│   │   ├── monitoring/
│   │   │   └── metrics.py
│   │   └── routes.py
│   ├── utils/
│   │   └── logger.py
│   ├── __init__.py
│   └── main.py
├── tests/
│   └── test_health.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore
```

## Monitoring Capabilities

This platform supports:

- API health tracking
- Request count monitoring
- Prometheus metrics exposure
- Latency and error pattern detection
- ML-based anomaly classification
- Structured application logs

## Future Enhancements

- Grafana dashboard integration
- PostgreSQL storage for historical metrics
- Alert notifications for anomalies
- CI/CD with GitHub Actions
- Cloud deployment on Render, Railway, AWS, or GCP
- Service-level objective tracking
- Real-time dashboard visualization

## Author

Kotesh Babu Bommana