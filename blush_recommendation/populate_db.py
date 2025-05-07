import sys
sys.path.append("/workspaces/BeautyColor")  # Add project directory to Python's path

from blush_recommendation.database.database import SessionLocal
import blush_recommendation.database.models as models

# Create a database session
db = SessionLocal()

# Sample data
skin_tones = [
    models.SkinTone(name="Fair"),
    models.SkinTone(name="Medium"),
    models.SkinTone(name="Deep"),
]

undertones = [
    models.Undertone(name="Warm"),
    models.Undertone(name="Cool"),
    models.Undertone(name="Neutral"),
]

recommendations = [
    models.BlushRecommendation(skin_tone_id=1, undertone_id=1, recommended_shades="Peach, Coral"),
    models.BlushRecommendation(skin_tone_id=2, undertone_id=2, recommended_shades="Rose, Berry"),
]

# Insert data
db.add_all(skin_tones)
db.add_all(undertones)
db.add_all(recommendations)

# Commit changes
db.commit()
db.close()

print("Sample data successfully inserted!")