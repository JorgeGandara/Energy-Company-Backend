from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from schemas.schema import VehicleSchema
from config.db import engine
from models.models import vehicle
from typing import List
# from werkzeug.utils import generate_password_hash, check_password_hash

router = APIRouter()

@router.get("/", response_model=List[VehicleSchema])
async def get_all_vehicle():
    with engine.connect() as conn:
        query = vehicle.select()
        return conn.execute(query).fetchall()
    
@router.get("/{idvehicle}", response_model=VehicleSchema)
async def get_vehicle(idvehicle: int):
    with engine.connect() as conn:
        query = vehicle.select().where(vehicle.c.idvehicle == idvehicle)
        return conn.execute(query).first()
    
@router.post("/", status_code=HTTP_201_CREATED)
async def create_vehicle(data_vehicle: VehicleSchema):
    with engine.connect() as conn:
        new_vehicle = data_vehicle.model_dump()
        conn.execute(vehicle.insert().values(new_vehicle))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)

@router.put("/{idvehicle}", response_model=VehicleSchema)
async def update_vehicle(idvehicle: int, data_vehicle: VehicleSchema):
    with engine.connect() as conn:
        query = vehicle.update().where(vehicle.c.idvehicle == idvehicle).values(data_vehicle.model_dump())
        conn.execute(query)
        conn.commit()
        return {"message": "Vehicle updated successfully"}

@router.delete("/{idvehicle}", status_code=HTTP_204_NO_CONTENT)
async def delete_vehicle(idvehicle: int):
    with engine.connect() as conn:
        query = vehicle.delete().where(vehicle.c.idvehicle == idvehicle)
        conn.execute(query)
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)