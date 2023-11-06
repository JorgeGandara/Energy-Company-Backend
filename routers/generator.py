from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from schemas.schema import GeneratorSchema
from config.db import engine
from models.models import generator
from typing import List

router = APIRouter()

@router.get("/", response_model=List[GeneratorSchema])
async def get_all_generator():
    with engine.connect() as conn:
        query = generator.select()
        return conn.execute(query).fetchall()
    
@router.get("/{idgenerator}", response_model = GeneratorSchema)
async def get_generator(idgenerator: int):
    with engine.connect() as conn:
        query = generator.select().where(generator.c.idgenerator == idgenerator)
        return conn.execute(query).first()
    
@router.post("/", status_code = HTTP_201_CREATED)
async def create_generator(data_generator: GeneratorSchema):
    with engine.connect() as conn:
        new_generator = data_generator.model_dump()
        conn.execute(generator.insert().values(new_generator))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)

@router.put("/{idgenerator}", response_model = GeneratorSchema)
async def update_generator(idgenerator: int, data_generator: GeneratorSchema):
    with engine.connect() as conn:
        query = generator.update().where(generator.c.idgenerator == idgenerator).values(data_generator.model_dump())
        conn.execute(query)
        conn.commit()
        return {"message": "Generator updated successfully"}

@router.delete("/{idgenerator}", status_code=HTTP_204_NO_CONTENT)
async def delete_generator(idgenerator: int):
    with engine.connect() as conn:
        query = generator.delete().where(generator.c.idgenerator == idgenerator)
        conn.execute(query)
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)