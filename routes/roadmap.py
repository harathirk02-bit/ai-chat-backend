from fastapi import APIRouter, Depends
from utils.jwt_handler import security
from services.roadmap_service import generate_roadmap

router = APIRouter()


# Generate Roadmap API
@router.get("/roadmap")
def roadmap(
    credentials = Depends(security)
):

    roadmap_data = generate_roadmap()

    return {
        "message": "Roadmap Generated",
        "roadmap": roadmap_data
    }