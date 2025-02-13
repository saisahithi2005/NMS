from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import LogEntry

router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/logs")
def get_logs(db: Session = Depends(get_db)):
    return db.query(LogEntry).all()

