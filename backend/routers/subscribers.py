from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import database, models, schemas
from .auth import get_current_user

router = APIRouter(
    prefix="/subscribers",
    tags=["subscribers"],
)

@router.post("/", response_model=schemas.Subscriber)
def subscribe(subscriber: schemas.SubscriberCreate, db: Session = Depends(database.get_db)):
    db_subscriber = db.query(models.Subscriber).filter(models.Subscriber.email == subscriber.email).first()
    if db_subscriber:
        if not db_subscriber.is_active:
            db_subscriber.is_active = True
            db.commit()
            db.refresh(db_subscriber)
            return db_subscriber
        raise HTTPException(status_code=400, detail="Email already subscribed")
    
    new_subscriber = models.Subscriber(email=subscriber.email)
    db.add(new_subscriber)
    db.commit()
    db.refresh(new_subscriber)
    return new_subscriber

@router.get("/", response_model=List[schemas.Subscriber])
def read_subscribers(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Not authorized")
    subscribers = db.query(models.Subscriber).offset(skip).limit(limit).all()
    return subscribers
