from fastapi import APIRouter, Depends, HTTPException, Path
from config.db import SessionLocal
from sqlalchemy.orm import Session
from schemas.schema import EmployeeSchema
from crud.employee import get_employee, get_employees, create_employee, update_employee, delete_employee

router = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@router.get("/{employee_id}", response_model=EmployeeSchema)
async def get_employee_by_id(employee_id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    db_employee = get_employee(db, employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

@router.get("/", response_model=list[EmployeeSchema])
async def get_all_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_employees = get_employees(db, skip, limit)
    return db_employees

@router.post("/", response_model=EmployeeSchema, status_code=201)
async def create_new_employee(employee: EmployeeSchema, db: Session = Depends(get_db)):
    db_employee = create_employee(db, employee)
    return db_employee

@router.put("/{employee_id}", response_model=EmployeeSchema)
async def update_employee_by_id(employee_id: int = Path(..., gt=0), employee: EmployeeSchema = Depends(), db: Session = Depends(get_db)):
    db_employee = get_employee(db, employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    db_employee = update_employee(db, employee_id, employee)
    return db_employee

@router.delete("/{employee_id}", response_model=EmployeeSchema)
async def delete_employee_by_id(employee_id: int = Path(..., gt=0), db: Session = Depends(get_db)):
    db_employee = get_employee(db, employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    db_employee = delete_employee(db, employee_id)
    return db_employee 
