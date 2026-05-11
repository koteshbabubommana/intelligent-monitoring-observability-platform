from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter(
    "api_request_count",
    "Total API Request Count"
)

REQUEST_LATENCY = Histogram(
    "api_request_latency_seconds",
    "API Request Latency"
)