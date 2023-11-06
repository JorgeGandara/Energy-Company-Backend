from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from schemas.schema import StateSchema
from config.db import engine
from models.models import state
from typing import List

router = APIRouter()

@router.get("/", response_model=List[StateSchema])
async def get_all_state():
    with engine.connect() as conn:
        query = state.select()
        return conn.execute(query).fetchall()
    
@router.get("/{idstate}", response_model = StateSchema)
async def get_state(idstate: int):
    with engine.connect() as conn:
        query = state.select().where(state.c.idstate == idstate)
        return conn.execute(query).first()
    
@router.post("/", status_code = HTTP_201_CREATED)
async def create_state(data_state: StateSchema):
    with engine.connect() as conn:
        new_state = data_state.model_dump()
        conn.execute(state.insert().values(new_state))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)

@router.put("/{idstate}", response_model = StateSchema)
async def update_state(idstate: int, data_state: StateSchema):
    with engine.connect() as conn:
        query = state.update().where(state.c.idstate == idstate).values(data_state.model_dump())
        conn.execute(query)
        conn.commit()
        return {"message": "State updated successfully"}

@router.delete("/{idstate}", status_code=HTTP_204_NO_CONTENT)
async def delete_state(idstate: int):
    with engine.connect() as conn:
        query = state.delete().where(state.c.idstate == idstate)
        conn.execute(query)
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)