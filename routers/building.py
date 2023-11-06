from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from schemas.schema import BuildingSchema
from config.db import engine
from models.models import building
from typing import List

router = APIRouter()

@router.get("/", response_model=List[BuildingSchema])
async def get_all_building():
    with engine.connect() as conn:
        query = building.select()
        return conn.execute(query).fetchall()
    
@router.get("/{idbuilding}", response_model = BuildingSchema)
async def get_building(idbuilding: int):
    with engine.connect() as conn:
        query = building.select().where(building.c.idbuilding == idbuilding)
        return conn.execute(query).first()
    
@router.post("/", status_code = HTTP_201_CREATED)
async def create_building(data_building: BuildingSchema):
    with engine.connect() as conn:
        new_building = data_building.model_dump()
        conn.execute(building.insert().values(new_building))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)

@router.put("/{idbuilding}", response_model = BuildingSchema)
async def update_building(idbuilding: int, data_building: BuildingSchema):
    with engine.connect() as conn:
        query = building.update().where(building.c.idbuilding == idbuilding).values(data_building.model_dump())
        conn.execute(query)
        conn.commit()
        return {"message": "Building updated successfully"}

@router.delete("/{idbuilding}", status_code=HTTP_204_NO_CONTENT)
async def delete_building(idbuilding: int):
    with engine.connect() as conn:
        query = building.delete().where(building.c.idbuilding == idbuilding)
        conn.execute(query)
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)