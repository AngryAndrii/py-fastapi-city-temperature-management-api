from fastapi import APIRouter

router = APIRouter()


@router.get("/temperatures/", tags=["temperatures"])
async def read_cities():
    return {"message": "Temperatures here!!!!!"}