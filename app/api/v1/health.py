from fastapi import APIRouter
# Create a router for API version 1
router = APIRouter()

@router.get("/health-check")
def check_health() -> dict[str, str]:
    return {
        "status" : "healthy",
        "service" : "RentFlow Backend"
    }
