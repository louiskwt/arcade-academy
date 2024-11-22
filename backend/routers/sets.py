from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_token_header

router = APIRouter(
    prefix="/sets",
    tags=["sets"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


fake_sets_db = {1: { "id": 1, "difficulty": "easy", "type": "word" }}

@router.get("/")
async def read_sets():
    return fake_sets_db

@router.get("/{set_id}")
async def read_set(set_id: int):
    if set_id not in fake_sets_db:
        raise HTTPException(status_code=404, detail="Set cannot be found.")
    return fake_sets_db[set_id]

