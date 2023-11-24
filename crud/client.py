from sqlalchemy.orm import Session
from models.models import Client
from schemas.schema import ClientSchema

def get_client(db: Session, client_id: int):
    return db.query(Client).filter(Client.idclient == client_id).first()

def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Client).offset(skip).limit(limit).all()

def create_client(db: Session, client: ClientSchema):
    db_client = Client(name=client.name, phone=client.phone, email=client.email, city=client.city, neighborhood=client.neighborhood, address=client.address, kw=client.kw)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def update_client(db: Session, client_id: int, client: ClientSchema):
    db_client = db.query(Client).filter(Client.idclient == client_id).first()
    db_client.name = client.name
    db_client.phone = client.phone
    db_client.email = client.email
    db_client.city = client.city
    db_client.neighborhood = client.neighborhood
    db_client.address = client.address
    db_client.kw = client.kw
    db.commit()
    db.refresh(db_client)
    return db_client

def delete_client(db: Session, client_id: int):
    db_client = db.query(Client).filter(Client.idclient == client_id).first()
    db.delete(db_client)
    db.commit()
    return db_client