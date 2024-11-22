from fastapi import Depends, FastAPI

from .dependencies import get_query_token
from .routers import users, sets

app = FastAPI()

app.include_router(users.router)
app.include_router(sets.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

