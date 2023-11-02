from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from schemas.schema import CutSchema
from config.db import engine
from models.models import cut
from typing import List

router = APIRouter()

@router.get("/", response_model=List[CutSchema])
async def get_all_cut():
    with engine.connect() as conn:
        query = cut.select()
        return conn.execute(query).fetchall()
    
@router.get("/{idcut}", response_model=CutSchema)
async def get_cut(idcut: int):
    with engine.connect() as conn:
        query = cut.select().where(cut.c.idcut == idcut)
        return conn.execute(query).first()
    
@router.post("/", status_code=HTTP_201_CREATED)
async def create_cut(data_cut: CutSchema):
    with engine.connect() as conn:
        new_cut = data_cut.model_dump()
        conn.execute(cut.insert().values(new_cut))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)

@router.put("/{idcut}", response_model=CutSchema)
async def update_cut(idcut: int, data_cut: CutSchema):
    with engine.connect() as conn:
        query = cut.update().where(cut.c.idcut == idcut).values(data_cut.model_dump())
        conn.execute(query)
        conn.commit()
        return {"message": "Cut updated successfully"}

@router.delete("/{idcut}", status_code=HTTP_204_NO_CONTENT)
async def delete_cut(idcut: int):
    with engine.connect() as conn:
        query = cut.delete().where(cut.c.idcut == idcut)
        conn.execute(query)
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)