from app.database.base import Base
from sqlalchemy import Column, String, Float, Enum, Integer, DateTime, func
import enum

class UserStatus(enum.Enum):
    FOOD = "FOOD"
    TRAVEL = "TRAVEL"
    SHOPPING = "SHOPPING"
    OTHERS = "OTHERS"


class Expense(Base):
    __tablename__ = "expenses"


    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(Enum(UserStatus), default=UserStatus.OTHERS)
    idempotency_key = Column(String(255), unique=True, index=True, nullable=True) # unique idempotency key to prevent duplicate expense input especially due to retries.
    created_at = Column(DateTime(timezone=True), server_default=func.now())

