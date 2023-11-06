from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, VARCHAR, Float, Boolean
from config.db import engine, meta_data

client = Table("client", meta_data,
    Column("idclient", Integer, primary_key=True, autoincrement=True),
    Column("name", VARCHAR(00)),
    Column("phone", Integer),
    Column("email", VARCHAR(80)),
    Column("city", VARCHAR(45)),
    Column("neighborhood", VARCHAR(45)),
    Column("address", VARCHAR(45)),
    Column("kw", Float)
)

employee = Table("employee", meta_data,
    Column("idemployee", Integer, primary_key=True, autoincrement=True),
    Column("name", VARCHAR(100)),
    Column("phone", Integer),
    Column("email", VARCHAR(80)),
    Column("city", VARCHAR(45)),
    Column("neighborhood", VARCHAR(45)),
    Column("address", VARCHAR(45)),
    Column("salary", Float),
)

cut = Table("cut", meta_data,
    Column("idcut", Integer, primary_key=True, autoincrement=True),
    Column("date", VARCHAR(10)),
    Column("hour", VARCHAR(10)),
    Column("city", VARCHAR(45)),
    Column("neighborhood", VARCHAR(45)),
)

state = Table("state", meta_data,
    Column("idstate", Integer, primary_key=True, autoincrement=True),
    Column("date", VARCHAR(10)),
    Column("hour", VARCHAR(10)),
    Column("description", VARCHAR(100)),
)

vehicle = Table("vehicle", meta_data,
    Column("idvehicle", Integer, primary_key=True, autoincrement=True),
    Column("name", VARCHAR(45)),
    Column("status", Boolean, nullable=False),
    Column("type", VARCHAR(45)),
    Column("km", Float),
    Column("function", VARCHAR(100))
)

building = Table("building", meta_data,
    Column("idbuilding", Integer, primary_key=True, autoincrement=True),
    Column("name", VARCHAR(45)),
    Column("status", Boolean, nullable=False),
    Column("phone", Integer),
)

generator = Table("generator", meta_data,
    Column("idgenerator", Integer, primary_key=True, autoincrement=True),
    Column("name", VARCHAR(45)),
    Column("status", Boolean, nullable=False),
    Column("eco", Integer),
    Column("power", Float),
)

meta_data.create_all(engine)