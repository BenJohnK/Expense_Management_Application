from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database.base import Base
from app.database.models import Expense
from app.session.session import engine
from app.api.expense_apis import router

app = FastAPI()

app.include_router(router)

@app.on_event("startup")
def startup_event():
    # This creates the tables defined in your models if they don't already exist
    Base.metadata.create_all(bind=engine)
    print("Database tables initialized.")


