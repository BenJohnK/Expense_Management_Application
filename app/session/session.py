from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# 1. Define your URL (Replace with your actual credentials or env variable)
DATABASE_URL = "postgresql://expense_user:myexam1234@localhost:5432/expense_db"

# 2. Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# 3. Create a SessionLocal class for creating database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# 5. Dependency to get the DB session in FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()