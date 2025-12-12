from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import database, models, schemas
from .auth import get_current_user

router = APIRouter(
    prefix="/newsletters",
    tags=["newsletters"],
)

@router.get("/", response_model=List[schemas.Newsletter])
def read_newsletters(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    newsletters = db.query(models.Newsletter).order_by(models.Newsletter.published_at.desc()).offset(skip).limit(limit).all()
    return newsletters

@router.get("/{newsletter_id}", response_model=schemas.Newsletter)
def read_newsletter(newsletter_id: int, db: Session = Depends(database.get_db)):
    newsletter = db.query(models.Newsletter).filter(models.Newsletter.id == newsletter_id).first()
    if not newsletter:
        raise HTTPException(status_code=404, detail="Newsletter not found")
    return newsletter

@router.post("/", response_model=schemas.Newsletter)
def create_newsletter(newsletter: schemas.NewsletterCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    db_newsletter = models.Newsletter(**newsletter.dict())
    db.add(db_newsletter)
    db.commit()
    db.refresh(db_newsletter)
    return db_newsletter
