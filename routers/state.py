from fastapi import APIRouter, Depends, HTTPException, Path
from config.db import SessionLocal
from sqlalchemy.orm import Session
from schemas.schema import StateSchema
from crud.state import get_state, get_states, create_state, update_state, delete_state

router = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.get("/{state_id}", response_model=StateSchema)
async def get_state_by_id(state_id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    db_state = get_state(db, state_id)
    if db_state is None:
        raise HTTPException(status_code=404, detail="State not found")
    return db_state

@router.get("/", response_model=list[StateSchema])
async def get_all_states(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_states = get_states(db, skip, limit)
    return db_states

@router.post("/", response_model=StateSchema, status_code=201)
async def create_new_state(state: StateSchema, db: Session = Depends(get_db)):
    db_state = create_state(db, state)
    return db_state

@router.put("/{state_id}", response_model=StateSchema)
async def update_state_by_id(state_id: int = Path(..., gt=0), state: StateSchema = Depends(), db: Session = Depends(get_db)):
    db_state = get_state(db, state_id)
    if db_state is None:
        raise HTTPException(status_code=404, detail="State not found")
    db_state = update_state(db, state_id, state)
    return db_state

@router.delete("/{state_id}", response_model=StateSchema)
async def delete_state_by_id(state_id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    db_state = get_state(db, state_id)
    if db_state is None:
        raise HTTPException(status_code=404, detail="State not found")
    db_state = delete_state(db, state_id)
    return db_state