from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# _address = os.environ.get('SQLALCHEMY_DATABASE_URI')
_address = "mysql+pymysql://root@localhost:3306/testdb"
_engine = create_engine(_address)
_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=_engine)


# db instance provider
def get_db_instance():
    db = _SessionLocal()
    try:
        yield db
    finally:
        db.close()
