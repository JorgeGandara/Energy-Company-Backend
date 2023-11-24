from sqlalchemy.orm import Session
from models.models import Vehicle
from schemas.schema import ClientSchema

def get_vehicle(db: Session, vehicle_id: int):
    return db.query(Vehicle).filter(Vehicle.idvehicle == vehicle_id).first()

def get_vehicles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Vehicle).offset(skip).limit(limit).all()

def create_vehicle(db: Session, vehicle: ClientSchema):
    db_vehicle = Vehicle(name=vehicle.name, status=vehicle.status, type=vehicle.type, km=vehicle.km, function=vehicle.function)
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

def update_vehicle(db: Session, vehicle_id: int, vehicle: ClientSchema):
    db_vehicle = db.query(Vehicle).filter(Vehicle.idvehicle == vehicle_id).first()
    db_vehicle.name = vehicle.name
    db_vehicle.status = vehicle.status
    db_vehicle.type = vehicle.type
    db_vehicle.km = vehicle.km
    db_vehicle.function = vehicle.function
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

def delete_vehicle(db: Session, vehicle_id: int):
    db_vehicle = db.query(Vehicle).filter(Vehicle.idvehicle == vehicle_id).first()
    db.delete(db_vehicle)
    db.commit()
    return db_vehicle
