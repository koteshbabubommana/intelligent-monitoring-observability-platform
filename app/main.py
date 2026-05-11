from fastapi import FastAPI
from prometheus_client import make_asgi_app

from app.api.routes import router

app = FastAPI(
    title="Intelligent Monitoring & Observability Platform",
    version="1.0.0"
)

app.include_router(router)

metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)