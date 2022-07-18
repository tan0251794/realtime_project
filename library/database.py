from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

username = 'tanlc'
password = '123456'
host = 'localhost'
db_name = 'my_db'

engine = create_engine(f"mariadb+pymysql://{username}:{password}@{host}/{db_name}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
