import os
from sqlalchemy import create_engine, MetaData

db_username = os.getenv('DB_USERNAME', 'energycompanydb')
db_password = os.getenv('DB_PASSWORD', 123456)
db_host = os.getenv('DB_HOST', "35.188.4.223")
db_port = int(os.getenv('PORT', 3306))
db_name = os.getenv('DB_DBNAME', 'energy_company')

engine = create_engine(f"mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}")

meta_data = MetaData()
meta_data.bind = engine