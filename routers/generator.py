from fastapi import APIRouter, Depends, HTTPException, Path
from config.db import SessionLocal
from sqlalchemy.orm import Session
from schemas.schema import GeneratorSchema
from crud.generator import get_generator, get_generators, create_generator, update_generator, delete_generator

router = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.get("/{generator_id}", response_model=GeneratorSchema)
async def get_generator_by_id(generator_id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    db_generator = get_generator(db, generator_id)
    if db_generator is None:
        raise HTTPException(status_code=404, detail="Generator not found")
    return db_generator

@router.get("/", response_model=list[GeneratorSchema])
async def get_all_generators(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_generators = get_generators(db, skip, limit)
    return db_generators

@router.post("/", response_model=GeneratorSchema, status_code=201)
async def create_new_generator(generator: GeneratorSchema, db: Session = Depends(get_db)):
    db_generator = create_generator(db, generator)
    return db_generator

@router.put("/{generator_id}", response_model=GeneratorSchema)
async def update_generator_by_id(generator_id: int = Path(..., gt=0), generator: GeneratorSchema = Depends(), db: Session = Depends(get_db)):
    db_generator = get_generator(db, generator_id)
    if db_generator is None:
        raise HTTPException(status_code=404, detail="Generator not found")
    db_generator = update_generator(db, generator_id, generator)
    return db_generator

@router.delete("/{generator_id}", response_model=GeneratorSchema)
async def delete_generator_by_id(generator_id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    db_generator = get_generator(db, generator_id)
    if db_generator is None:
        raise HTTPException(status_code=404, detail="Generator not found")
    db_generator = delete_generator(db, generator_id)
    return db_generator
