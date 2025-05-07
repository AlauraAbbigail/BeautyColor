from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from blush_recommendation.database.database import SessionLocal
import blush_recommendation.database.models as models

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/recommendations/{skin_tone}/{undertone}")
def get_recommendations(skin_tone: str, undertone: str, db: Session = Depends(get_db)):
    recommendations = (
        db.query(models.BlushRecommendation)
        .filter(models.BlushRecommendation.skin_tone_id == skin_tone)
        .filter(models.BlushRecommendation.undertone_id == undertone)
        .first()
    )
    if recommendations:
        return {"blush_shades": recommendations.recommended_shades.split(", ")}
    return {"message": "No recommendation found for this combination"}