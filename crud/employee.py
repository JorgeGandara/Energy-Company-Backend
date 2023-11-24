from sqlalchemy.orm import Session
from models.models import Employee
from schemas.schema import EmployeeSchema

def get_employee(db: Session, employee_id: int):
    return db.query(Employee).filter(Employee.idemployee == employee_id).first()

def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Employee).offset(skip).limit(limit).all()

def create_employee(db: Session, employee: EmployeeSchema):
    db_employee = Employee(name=employee.name, phone=employee.phone, email=employee.email, city=employee.city, neighborhood=employee.neighborhood, address=employee.address, salary=employee.salary)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def update_employee(db: Session, employee_id: int, employee: EmployeeSchema):
    db_employee = db.query(Employee).filter(Employee.idemployee == employee_id).first()
    db_employee.name = employee.name
    db_employee.phone = employee.phone
    db_employee.email = employee.email
    db_employee.city = employee.city
    db_employee.neighborhood = employee.neighborhood
    db_employee.address = employee.address
    db_employee.salary = employee.salary
    db.commit()
    db.refresh(db_employee)
    return db_employee

def delete_employee(db: Session, employee_id: int):
    db_employee = db.query(Employee).filter(Employee.idemployee == employee_id).first()
    db.delete(db_employee)
    db.commit()
    return db_employee