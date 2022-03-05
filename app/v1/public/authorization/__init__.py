from fastapi import (
    APIRouter,
)

from app.v1.public.authorization.getCode import getCode

auth = APIRouter(prefix="/authorization")

auth.include_router(getCode)

