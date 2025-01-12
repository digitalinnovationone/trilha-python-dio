from pydantic import BaseModel


class LoginIn(BaseModel):
    user_id: int
