from datetime import UTC, datetime
from typing import Annotated

from fastapi import Response, Cookie, status, Header, APIRouter
from schemas.post import PostIn
from views.post import PostOut

router = APIRouter(prefix="/posts")

fake_db =[
    {"title": "Criando uma aplicação com Django", "date": datetime.now(UTC), 'published': True },
    {"title": "Criando uma aplicação com FastAPI", "date": datetime.now(UTC), 'published': True},
    {"title": "Criando uma aplicação com Flask", "date": datetime.now(UTC), 'published': True },
    {"title": "Criando uma aplicação com Starlette", "date": datetime.now(UTC), 'published': False },
]

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
def create_post(post: PostIn):
    fake_db.append(post.model_dump())
    return post

@router.get("/", response_model=list[PostOut])
def read_posts(
    response: Response, 
    published: bool, 
    limit: int, 
    skip: int = 0, 
    ads_id: Annotated[str | None, Cookie()] = None, 
    user_agent: Annotated[str | None, Header()] = None,
):
    
    response.set_cookie(key="mhss", value="MHDEV")
    print(f"Cookie: {ads_id}")
    print(f"User-Agent: {user_agent}")
    tail = skip + limit
    return [post for post in fake_db[skip : tail] if post['published'] is published]

@router.get("/{framework}", response_model=PostOut)
def read_framework_posts(framework: str):
    return {
        "posts": [
            {"title": f"Criando uma aplicação com {framework}", "date": datetime.now(UTC)},
            {"title": f"Internacionalizando uma app {framework}", "date": datetime.now(UTC)},
        ]
    }