from fastapi import APIRouter, Depends, HTTPException
from app.session.session import get_db
from sqlalchemy.orm import Session
from app.database.models import Expense
from .schemas import ExpenseCreate


router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)


@router.get("/")
def get_all_expenses(db: Session = Depends(get_db)):
    # Fetch all records from the expenses table
    expenses = db.query(Expense).all()
    return expenses

@router.post("/", status_code=201)
def create_expense(expense_data: ExpenseCreate, db: Session = Depends(get_db)):
    # 1. Create the model instance from request data
    new_expense = Expense(
        name=expense_data.name,
        amount=expense_data.amount,
        category=expense_data.category,
        idempotency_key=expense_data.idempotency_key
    )
    
    # 2. Add and commit to DB
    try:
        db.add(new_expense)
        db.commit()
        db.refresh(new_expense) # Refreshes to get the auto-generated ID and timestamp
        return new_expense
    except Exception as e:
        db.rollback() # Rollback if something goes wrong (like a duplicate idempotency key)
        raise HTTPException(status_code=400, detail="Could not create expense. Check for duplicate keys.")