# Intelligent Monitoring & Observability Platform

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)
![Prometheus](https://img.shields.io/badge/Prometheus-Metrics-orange)
![Machine Learning](https://img.shields.io/badge/ML-AnomalyDetection-red)
![Status](https://img.shields.io/badge/Status-Active-success)

A scalable backend monitoring and observability platform for tracking API health, request metrics, latency signals, and anomaly patterns using FastAPI, Prometheus metrics, Docker, and machine learning based anomaly detection.

---

# Features

- REST API monitoring with FastAPI
- Real-time request metrics collection
- API latency tracking
- Machine learning based anomaly detection
- Prometheus metrics integration
- Structured logging system
- Docker containerization
- Health monitoring endpoints
- Scalable backend architecture
- Automated API testing

---

# Architecture

```text
Client / API User
        |
        v
FastAPI Backend
        |
        +-------------------+
        |                   |
        v                   v
Monitoring Layer      ML Anomaly Detection
        |                   |
        v                   v
Prometheus Metrics     Isolation Forest Model
        |
        v
Logging & Observability
```

---

# Tech Stack

## Backend
- Python
- FastAPI
- Uvicorn

## Machine Learning
- Scikit-learn
- Isolation Forest

## Monitoring & Observability
- Prometheus Client
- Structured Logging

## DevOps & Infrastructure
- Docker
- Docker Compose

## Testing
- Pytest

---

# Project Structure

```text
intelligent-monitoring-observability-platform/
│
├── app/
│   ├── api/
│   │   ├── ml/
│   │   │   └── anomaly_detector.py
│   │   ├── monitoring/
│   │   │   └── metrics.py
│   │   └── routes.py
│   │
│   ├── utils/
│   │   └── logger.py
│   │
│   ├── __init__.py
│   └── main.py
│
├── tests/
│   └── test_health.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# API Endpoints

## Home Endpoint

```http
GET /
```

Response:

```json
{
  "message": "Intelligent Monitoring Platform Running"
}
```

---

## Health Check Endpoint

```http
GET /health
```

Response:

```json
{
  "status": "healthy"
}
```

---

## Anomaly Detection Endpoint

```http
GET /detect-anomaly
```

Parameters:

| Parameter | Type | Description |
|---|---|---|
| latency_ms | float | API latency |
| error_count | int | Number of API errors |
| request_count | int | Total request count |

Example:

```http
/detect-anomaly?latency_ms=900&error_count=12&request_count=500
```

Example Response:

```json
{
  "latency_ms": 900,
  "error_count": 12,
  "request_count": 500,
  "anomaly_score": -0.24,
  "is_anomaly": true
}
```

---

## Metrics Endpoint

```http
GET /metrics
```

Used for Prometheus metrics scraping and monitoring.

---

# Installation

## Clone Repository

```bash
git clone https://github.com/koteshbabubommana/intelligent-monitoring-observability-platform.git
```

---

## Navigate to Project

```bash
cd intelligent-monitoring-observability-platform
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Application

```bash
uvicorn app.main:app --reload
```

Application runs on:

```text
http://127.0.0.1:8000
```

---

# Swagger API Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

---

# Run Tests

```bash
pytest
```

---

# Docker Setup

## Build Container

```bash
docker build -t monitoring-platform .
```

---

## Run Container

```bash
docker run -p 8000:8000 monitoring-platform
```

---

# Future Enhancements

- Grafana dashboard integration
- Kafka event streaming
- Redis caching layer
- Kubernetes deployment
- CI/CD pipeline automation
- JWT authentication
- Real-time monitoring dashboard
- AWS cloud deployment
- Distributed tracing
- Alerting system integration

---

# Key Engineering Concepts Demonstrated

- Backend API development
- Distributed systems concepts
- Observability engineering
- Monitoring systems
- Machine learning integration
- Production-style logging
- API performance tracking
- Containerization
- Service health monitoring
- Scalable backend architecture

---

# Author

## Kotesh Babu Bommana

Software Engineer focused on backend systems, distributed systems, APIs, cloud infrastructure, and scalable monitoring platforms.

- LinkedIn: https://www.linkedin.com/in/kotesh-babu-bommana
- GitHub: https://github.com/koteshbabubommana