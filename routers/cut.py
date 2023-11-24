from fastapi import APIRouter, Depends, HTTPException, Path
from config.db import SessionLocal
from sqlalchemy.orm import Session
from schemas.schema import CutSchema
from crud.cut import get_cut, get_cuts, create_cut, update_cut, delete_cut

router = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.get("/{cut_id}", response_model=CutSchema)
async def get_cut_by_id(cut_id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    db_cut = get_cut(db, cut_id)
    if db_cut is None:
        raise HTTPException(status_code=404, detail="Cut not found")
    return db_cut

@router.get("/", response_model=list[CutSchema])
async def get_all_cuts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_cuts = get_cuts(db, skip, limit)
    return db_cuts

@router.post("/", response_model=CutSchema, status_code=201)
async def create_new_cut(cut: CutSchema, db: Session = Depends(get_db)):
    db_cut = create_cut(db, cut)
    return db_cut

@router.put("/{cut_id}", response_model=CutSchema)
async def update_cut_by_id(cut_id: int = Path(..., gt=0), cut: CutSchema = Depends(), db: Session = Depends(get_db)):
    db_cut = get_cut(db, cut_id)
    if db_cut is None:
        raise HTTPException(status_code=404, detail="Cut not found")
    db_cut = update_cut(db, cut_id, cut)
    return db_cut

@router.delete("/{cut_id}", response_model=CutSchema)
async def delete_cut_by_id(cut_id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    db_cut = get_cut(db, cut_id)
    if db_cut is None:
        raise HTTPException(status_code=404, detail="Cut not found")
    db_cut = delete_cut(db, cut_id)
    return db_cut
