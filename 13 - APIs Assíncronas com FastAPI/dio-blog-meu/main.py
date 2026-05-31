from fastapi import FastAPI
# para rodar o app: uvicorn main:app --reload

from controllers import post

app = FastAPI()
app.include_router(post.router)