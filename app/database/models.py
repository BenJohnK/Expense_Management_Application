from app.database.base import Base
from sqlalchemy import Column, String, Float, Enum


class UserStatus(Enum):
    FOOD = "FOOD"
    TRAVEL = "TRAVEL"
    SHOPPING = "SHOPPING"
    OTHERS = "OTHERS"


class Expense(Base):
    name = Column(String(100), nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(Enum(UserStatus), default=UserStatus.OTHERS)

