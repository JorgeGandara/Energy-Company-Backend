from fastapi import APIRouter, Depends, HTTPException, Path
from config.db import SessionLocal
from sqlalchemy.orm import Session
from schemas.schema import BuildingSchema
from crud.building import get_building, get_buildings, create_building, update_building, delete_building

router = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.get("/{building_id}", response_model=BuildingSchema)
async def get_building_by_id(building_id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    db_building = get_building(db, building_id)
    if db_building is None:
        raise HTTPException(status_code=404, detail="Building not found")
    return db_building

@router.get("/", response_model=list[BuildingSchema])
async def get_all_buildings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_buildings = get_buildings(db, skip, limit)
    return db_buildings

@router.post("/", response_model=BuildingSchema, status_code=201)
async def create_new_building(building: BuildingSchema, db: Session = Depends(get_db)):
    db_building = create_building(db, building)
    return db_building

@router.put("/{building_id}", response_model=BuildingSchema)
async def update_building_by_id(building_id: int = Path(..., gt=0), building: BuildingSchema = Depends(), db: Session = Depends(get_db)):
    db_building = get_building(db, building_id)
    if db_building is None:
        raise HTTPException(status_code=404, detail="Building not found")
    db_building = update_building(db, building_id, building)
    return db_building

@router.delete("/{building_id}", response_model=BuildingSchema)
async def delete_building_by_id(building_id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    db_building = get_building(db, building_id)
    if db_building is None:
        raise HTTPException(status_code=404, detail="Building not found")
    db_building = delete_building(db, building_id)
    return db_building
