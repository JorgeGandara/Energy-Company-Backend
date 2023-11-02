from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from schemas.schema import EmployeeSchema
from config.db import engine
from models.models import employee
from typing import List

router = APIRouter()

@router.get("/", response_model=List[EmployeeSchema])
async def get_all_employee():
    with engine.connect() as conn:
        query = employee.select()
        return conn.execute(query).fetchall()
    
@router.get("/{idemployee}", response_model=EmployeeSchema)
async def get_employee(idemployee: int):
    with engine.connect() as conn:
        query = employee.select().where(employee.c.idemployee == idemployee)
        return conn.execute(query).first()
    
@router.post("/", status_code=HTTP_201_CREATED)
async def create_employee(data_employee: EmployeeSchema):
    with engine.connect() as conn:
        new_employee = data_employee.model_dump()
        conn.execute(employee.insert().values(new_employee))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)

@router.put("/{idemployee}", response_model=EmployeeSchema)
async def update_employee(idemployee: int, data_employee: EmployeeSchema):
    with engine.connect() as conn:
        query = employee.update().where(employee.c.idemployee == idemployee).values(data_employee.model_dump())
        conn.execute(query)
        conn.commit()
        return {"message": "Employee updated successfully"}

@router.delete("/{idemployee}", status_code=HTTP_204_NO_CONTENT)
async def delete_employee(idemployee: int):
    with engine.connect() as conn:
        query = employee.delete().where(employee.c.idemployee == idemployee)
        conn.execute(query)
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)