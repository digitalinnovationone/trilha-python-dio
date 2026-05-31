from datetime import UTC, datetime
from pydantic import BaseModel

class PostOut(BaseModel):
    title: str
    date: datetime