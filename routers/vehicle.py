from fastapi import APIRouter, Depends, HTTPException, Path
from config.db import SessionLocal
from sqlalchemy.orm import Session
from schemas.schema import VehicleSchema
from crud.vehicle import get_vehicle, get_vehicles, create_vehicle, update_vehicle, delete_vehicle

router = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.get("/{vehicle_id}", response_model=VehicleSchema)
async def get_vehicle_by_id(vehicle_id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    db_vehicle = get_vehicle(db, vehicle_id)
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return db_vehicle

@router.get("/", response_model=list[VehicleSchema])
async def get_all_vehicles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_vehicles = get_vehicles(db, skip, limit)
    return db_vehicles

@router.post("/", response_model=VehicleSchema, status_code=201)
async def create_new_vehicle(vehicle: VehicleSchema, db: Session = Depends(get_db)):
    db_vehicle = create_vehicle(db, vehicle)
    return db_vehicle

@router.put("/{vehicle_id}", response_model=VehicleSchema)
async def update_vehicle_by_id(vehicle_id: int = Path(..., gt=0), vehicle: VehicleSchema = Depends(), db: Session = Depends(get_db)):
    db_vehicle = get_vehicle(db, vehicle_id)
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    db_vehicle = update_vehicle(db, vehicle_id, vehicle)
    return db_vehicle

@router.delete("/{vehicle_id}", response_model=VehicleSchema)
async def delete_vehicle_by_id(vehicle_id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    db_vehicle = get_vehicle(db, vehicle_id)
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    db_vehicle = delete_vehicle(db, vehicle_id)
    return db_vehicle
