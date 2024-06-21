from pydantic import BaseModel


class LoginOut(BaseModel):
    access_token: str
