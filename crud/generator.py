from sqlalchemy.orm import Session
from models.models import Generator
from schemas.schema import GeneratorSchema

def get_generator(db: Session, generator_id: int):
    return db.query(Generator).filter(Generator.idgenerator == generator_id).first()

def get_generators(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Generator).offset(skip).limit(limit).all()

def create_generator(db: Session, generator: GeneratorSchema):
    db_generator = Generator(id=generator.idgenerator, name=generator.name, status=generator.status, eco=generator.eco, power=generator.power)
    db.add(db_generator)
    db.commit()
    db.refresh(db_generator)
    return db_generator

def update_generator(db: Session, generator_id: int, generator: GeneratorSchema):
    db_generator = db.query(Generator).filter(Generator.idgenerator == generator_id).first()
    db_generator.name = generator.name
    db_generator.status = generator.status
    db_generator.eco = generator.eco
    db_generator.power = generator.power
    db.commit()
    db.refresh(db_generator)
    return db_generator

def delete_generator(db: Session, generator_id: int):
    db_generator = db.query(Generator).filter(Generator.idgenerator == generator_id).first()
    db.delete(db_generator)
    db.commit()
    return db_generator