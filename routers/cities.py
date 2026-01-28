from fastapi import APIRouter

router = APIRouter()


@router.get("/cities/", tags=["cities"])
async def read_cities():
    return {"message": "Cities here!!!"}