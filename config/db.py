from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://energycompanydb:123456@35.188.4.223:3306/energy_company")

meta_data = MetaData()
meta_data.bind = engine