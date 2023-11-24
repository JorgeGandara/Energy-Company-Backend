from fastapi import APIRouter, Depends, HTTPException, Path
from config.db import SessionLocal
from sqlalchemy.orm import Session
from schemas.schema import ClientSchema
from crud.client import get_client, get_clients, create_client, update_client, delete_client

router = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.get("/{client_id}", response_model=ClientSchema)
async def get_client_by_id(client_id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    db_client = get_client(db, client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    return db_client

@router.get("/", response_model=list[ClientSchema])
async def get_all_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_clients = get_clients(db, skip, limit)
    return db_clients

@router.post("/", response_model=ClientSchema, status_code=201)
async def create_new_client(client: ClientSchema, db: Session = Depends(get_db)):
    db_client = create_client(db, client)
    return db_client

@router.put("/{client_id}", response_model=ClientSchema)
async def update_client_by_id(client_id: int = Path(..., gt=0), client: ClientSchema = Depends(), db: Session = Depends(get_db)):
    db_client = get_client(db, client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    db_client = update_client(db, client_id, client)
    return db_client

@router.delete("/{client_id}", response_model=ClientSchema)
async def delete_client_by_id(client_id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    db_client = get_client(db, client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Client not found")
    db_client = delete_client(db, client_id)
    return db_client