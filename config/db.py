from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:123456@localhost:3306/energy_company")

meta_data = MetaData()
meta_data.bind = engine