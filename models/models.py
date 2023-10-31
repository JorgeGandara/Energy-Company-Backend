from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, VARCHAR, Float, Boolean
from config.db import engine, meta_data

vehicle = Table("vehicle", meta_data,
    Column("idvehicle", Integer, primary_key=True),
    Column("name", VARCHAR(45)),
    Column("status", Boolean, nullable=False),
    Column("type", VARCHAR(45)),
    Column("km", Float),
    Column("function", VARCHAR(100))
)

meta_data.create_all(engine)