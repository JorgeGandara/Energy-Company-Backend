from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from schemas.schema import ClientSchema
from config.db import engine
from models.models import client
from typing import List
# from werkzeug.utils import generate_password_hash, check_password_hash

router = APIRouter()

@router.get("/", response_model=List[ClientSchema])
async def get_all_client():
    with engine.connect() as conn:
        query = client.select()
        return conn.execute(query).fetchall()
    
@router.get("/{idclient}", response_model=ClientSchema)
async def get_client(idclient: int):
    with engine.connect() as conn:
        query = client.select().where(client.c.idclient == idclient)
        return conn.execute(query).first()
    
@router.post("/", status_code=HTTP_201_CREATED)
async def create_client(data_client: ClientSchema):
    with engine.connect() as conn:
        new_client = data_client.model_dump()
        conn.execute(client.insert().values(new_client))
        conn.commit()
        return Response(status_code=HTTP_201_CREATED)

@router.put("/{idclient}", response_model=ClientSchema)
async def update_client(idclient: int, data_client: ClientSchema):
    with engine.connect() as conn:
        query = client.update().where(client.c.idclient == idclient).values(data_client.model_dump())
        conn.execute(query)
        conn.commit()
        return {"message": "Client updated successfully"}

@router.delete("/{idclient}", status_code=HTTP_204_NO_CONTENT)
async def delete_client(idclient: int):
    with engine.connect() as conn:
        query = client.delete().where(client.c.idclient == idclient)
        conn.execute(query)
        conn.commit()
        return Response(status_code=HTTP_204_NO_CONTENT)