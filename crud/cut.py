from sqlalchemy.orm import Session
from models.models import Cut
from schemas.schema import CutSchema

def get_cut(db: Session, cut_id: int):
    return db.query(Cut).filter(Cut.idcut == cut_id).first()

def get_cuts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Cut).offset(skip).limit(limit).all()

def create_cut(db: Session, cut: CutSchema):
    db_cut = Cut(date=cut.date, hour=cut.hour, city=cut.city, neighborhood=cut.neighborhood)
    db.add(db_cut)
    db.commit()
    db.refresh(db_cut)
    return db_cut

def update_cut(db: Session, cut_id: int, cut: CutSchema):
    db_cut = db.query(Cut).filter(Cut.idcut == cut_id).first()
    db_cut.date = cut.date
    db_cut.hour = cut.hour
    db_cut.city = cut.city
    db_cut.neighborhood = cut.neighborhood
    db.commit()
    db.refresh(db_cut)
    return db_cut

def delete_cut(db: Session, cut_id: int):
    db_cut = db.query(Cut).filter(Cut.idcut == cut_id).first()
    db.delete(db_cut)
    db.commit()
    return db_cut