from sqlalchemy.orm import Session
from models.models import Building
from schemas.schema import BuildingSchema

def get_building(db: Session, building_id: int):
    return db.query(Building).filter(Building.idbuilding == building_id).first()

def get_buildings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Building).offset(skip).limit(limit).all()

def create_building(db: Session, building: BuildingSchema):
    db_building = Building(name=building.name, status=building.status, phone=building.phone, email=building.email, city=building.city, neighborhood=building.neighborhood, address=building.address, kw=building.kw)
    db.add(db_building)
    db.commit()
    db.refresh(db_building)
    return db_building

def update_building(db: Session, building_id: int, building: BuildingSchema):
    db_building = db.query(Building).filter(Building.idbuilding == building_id).first()
    db_building.name = building.name
    db_building.status = building.status
    db_building.phone = building.phone
    db.commit()
    db.refresh(db_building)
    return db_building