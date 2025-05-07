from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from blush_recommendation.database.database import Base

class SkinTone(Base):
    __tablename__ = "skin_tones"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class Undertone(Base):
    __tablename__ = "undertones"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class BlushRecommendation(Base):
    __tablename__ = "blush_recommendations"
    id = Column(Integer, primary_key=True)
    skin_tone_id = Column(Integer, ForeignKey("skin_tones.id"))
    undertone_id = Column(Integer, ForeignKey("undertones.id"))
    recommended_shades = Column(String)  # Store shades as comma-separated values

    skin_tone = relationship("SkinTone")
    undertone = relationship("Undertone")
