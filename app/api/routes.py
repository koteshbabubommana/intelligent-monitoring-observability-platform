from fastapi import APIRouter
from app.api.ml.anomaly_detector import detect_anomaly
from app.api.monitoring.metrics import REQUEST_COUNT
from app.utils.logger import logger

router = APIRouter()


@router.get("/")
def home():
    REQUEST_COUNT.inc()
    logger.info("Home endpoint accessed")

    return {
        "message": "Intelligent Monitoring & Observability Platform Running"
    }


@router.get("/health")
def health_check():
    REQUEST_COUNT.inc()
    logger.info("Health check endpoint accessed")

    return {
        "status": "healthy"
    }


@router.get("/detect-anomaly")
def anomaly_detection(
    latency_ms: float,
    error_count: int,
    request_count: int
):
    REQUEST_COUNT.inc()

    result = detect_anomaly(
        latency_ms,
        error_count,
        request_count
    )

    logger.info(f"Anomaly detection result: {result}")

    return result