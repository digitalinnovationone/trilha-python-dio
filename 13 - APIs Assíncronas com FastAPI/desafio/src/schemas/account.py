from pydantic import BaseModel, PositiveFloat
from typing import Optional

class AccountCreate(BaseModel):
    balance: Optional[PositiveFloat] = 0.0

class AccountOut(BaseModel):
    id: int
    user_id: int
    balance: float
    created_at: str  # o view usa AwareDatetime/NaiveDatetime; aqui deixei string para compatibilidade simples

    class Config:
        orm_mode = True

