from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from blush_recommendation.database.database import SessionLocal
import blush_recommendation.database.models as models

router = APIRouter(prefix="/recommendations")  # ✅ Prefix ensures correct path

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{skin_tone}/{undertone}")  # ✅ Path now aligns with prefix
def get_recommendations(skin_tone: str, undertone: str, db: Session = Depends(get_db)):
    recommendations = (
    db.query(models.BlushRecommendation)
    .join(models.SkinTone)
    .join(models.Undertone)
    .filter(models.SkinTone.name == skin_tone)
    .filter(models.Undertone.name == undertone)
    .first()

    if recommendations:
        return {"blush_shades": recommendations.recommended_shades.split(", ")}
    return {"message": "No recommendation found for this combination"}
