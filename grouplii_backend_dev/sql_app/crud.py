from sqlalchemy.orm import Session
from . import models, schemas


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.InventoryDetailTable).offset(skip).limit(limit).all()