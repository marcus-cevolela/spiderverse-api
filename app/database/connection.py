from sqlalchemy import create_engine
from app.core.settings import settings
from sqlalchemy.orm import sessionmaker

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def get_db ():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()