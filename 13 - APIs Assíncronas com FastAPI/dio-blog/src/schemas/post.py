from pydantic import AwareDatetime, BaseModel


class PostIn(BaseModel):
    title: str
    content: str
    published_at: AwareDatetime | None = None
    published: bool = False


class PostUpdateIn(BaseModel):
    title: str | None = None
    content: str | None = None
    published_at: AwareDatetime | None = None
    published: bool | None = None
