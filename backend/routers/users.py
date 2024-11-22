from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_token_header

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


fake_users_db = {1: { "id": 1, "xp": 0 }}

@router.get("/")
async def read_users():
    return fake_users_db

@router.get("/{user_id}")
async def read_user(user_id: int):
    if user_id not in fake_users_db:
        raise HTTPException(status_code=404, detail="User cannot be found.")
    return fake_users_db[user_id]

