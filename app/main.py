from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.health import router as health_router

# 1. Initialize the main FastAPI application
app = FastAPI(
    title = settings.PROJECT_NAME,
    version = settings.PROJECT_VERSION
)

# 2. Register the health router with prefix /api/v1

app.include_router(
    health_router,
    prefix = settings.API_V1_PREFIX, 
    tags = ["Health"]
)

# 3. Root endpoint
@app.get("/")
def read_root() -> dict[str, str]:
    return {
        "message" : f"Welcome to {settings.PROJECT_NAME}",
        "docs_url" : "/docs"
    }
