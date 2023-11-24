from sqlalchemy.orm import Session
from models.models import State
from schemas.schema import StateSchema

def get_state(db: Session, state_id: int):
    return db.query(State).filter(State.idstate == state_id).first()

def get_states(db: Session, skip: int = 0, limit: int = 100):
    return db.query(State).offset(skip).limit(limit).all()

def create_state(db: Session, state: StateSchema):
    db_state = State(idstate=state.idstate, date=state.date, hour=state.hour, description=state.description)
    db.add(db_state)
    db.commit()
    db.refresh(db_state)
    return db_state

def update_state(db: Session, state_id: int, state: StateSchema):
    db_state = db.query(State).filter(State.idstate == state_id).first()
    db_state.date = state.date
    db_state.hour = state.hour
    db_state.description = state.description
    db.commit()
    db.refresh(db_state)
    return db_state

def delete_state(db: Session, state_id: int):
    db_state = db.query(State).filter(State.idstate == state_id).first()
    db.delete(db_state)
    db.commit()
    return db_state