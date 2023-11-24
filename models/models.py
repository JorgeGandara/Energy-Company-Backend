from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, VARCHAR, Float, Boolean, String
from config.db import Base, engine

class Client(Base):
    __tablename__ = 'client'

    idclient = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    phone = Column(Integer)
    email = Column(Integer)
    city = Column(Integer)
    neighborhood = Column(Integer)
    address = Column(Integer)
    kw = Column(Float)

class Vehicle(Base):
    __tablename__ = 'vehicle'

    idvehicle = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    status = Column(Integer)
    type = Column(Integer)
    km = Column(Float)
    function = Column(Integer)

class Employee(Base):
    __tablename__ = 'employee'

    idemployee = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    phone = Column(Integer)
    email = Column(Integer)
    city = Column(Integer)
    neighborhood = Column(Integer)
    address = Column(Integer)
    salary = Column(Float)

class Cut(Base):
    __tablename__ = 'cut'

    idcut = Column(Integer, primary_key=True, index=True, autoincrement=True)
    date = Column(String)
    hour = Column(String)
    city = Column(String)
    neighborhood = Column(String)

class State(Base):
    __tablename__ = 'state'

    idstate = Column(Integer, primary_key=True, index=True, autoincrement=True)
    date = Column(String)
    hour = Column(String)
    description = Column(String)

class Building(Base):
    __tablename__ = 'building'

    idbuilding = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    status = Column(Integer)
    phone = Column(Integer)

class Generator(Base):
    __tablename__ = 'generator'

    idgenerator = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    status = Column(Integer)
    eco = Column(Integer)
    power = Column(Float)

Base.metadata.create_all(bind=engine)


