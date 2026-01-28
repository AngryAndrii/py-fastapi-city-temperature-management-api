from fastapi import FastAPI

from core import settings
from routers import *

app = FastAPI()

app.include_router(
    cities_router,
    prefix=settings.API_PREFIX,
)


#
# @app.get("/")
# async def root():
#     return {"message": "Hello Bigger Applications!"}