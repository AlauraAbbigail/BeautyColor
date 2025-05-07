from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import blush_recommendation.database.models as models
from blush_recommendation.database.database import SessionLocal, engine, Base

# Ensure tables are created
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/skin_tones/")
def read_skin_tones(db: Session = Depends(get_db)):
    return db.query(models.SkinTone).all()

@app.get("/undertones/")
def read_undertones(db: Session = Depends(get_db)):
    return db.query(models.Undertone).all()

@app.get("/")
def home():
    return {"message": "Welcome to the Blush Recommendor API!"}
