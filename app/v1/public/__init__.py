from fastapi import (
    APIRouter,
)
from app.v1.public.authorization import auth

public = APIRouter(prefix="/public")


@public.get("/ping")
async def ping_event():
    return {"message": "Pong!"}

public.include_router(auth)
