from pydantic import BaseModel
from typing import Optional
from app.database.models import UserStatus # Import your Enum

class ExpenseCreate(BaseModel):
    name: str
    amount: float
    category: UserStatus = UserStatus.OTHERS
    idempotency_key: Optional[str] = None # Optional, since we added it earlier

    