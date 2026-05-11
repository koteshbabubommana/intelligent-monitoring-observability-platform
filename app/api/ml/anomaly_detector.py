import numpy as np
from sklearn.ensemble import IsolationForest


def detect_anomaly(latency_ms: float, error_count: int, request_count: int):
    model = IsolationForest(contamination=0.2, random_state=42)

    training_data = np.array([
        [120, 1, 100],
        [140, 0, 120],
        [160, 2, 140],
        [180, 1, 160],
        [220, 3, 180],
        [900, 12, 500],
    ])

    model.fit(training_data)

    sample = np.array([[latency_ms, error_count, request_count]])

    prediction = model.predict(sample)[0]
    score = model.decision_function(sample)[0]

    return {
        "latency_ms": float(latency_ms),
        "error_count": int(error_count),
        "request_count": int(request_count),
        "anomaly_score": float(score),
        "is_anomaly": bool(prediction == -1)
    }