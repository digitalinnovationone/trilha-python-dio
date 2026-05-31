from pydantic import BaseModel, PositiveFloat


class AccountIn(BaseModel):
    name: str
    user_id: int
    balance: PositiveFloat
