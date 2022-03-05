import random

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Request
)
import datetime
import jwt
from fastapi_limiter.depends import RateLimiter
from pydantic import (
    BaseModel,
    validator
)
import re
from app.v1.api.database_user_api import (
    insert_user,
    user_exist,
    setAuthCode,
    get_user
)
from app.v1.api.smtp import send_code
getCode = APIRouter(prefix="/getCode")


class CodeRequest(BaseModel):
    email: str

    @validator("email")
    def email_regex(cls, v):
        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        if not re.fullmatch(regex, v):
            raise ValueError("Invalid email")
        return v


class CodeModel(BaseModel):
    email: str
    code: int

    @validator("email")
    def email_regex(cls, v):
        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        if not re.fullmatch(regex, v):
            raise ValueError("Invalid email")
        return v


@getCode.get("/test")
async def test_event():
    await send_code("csigorek@gmail.com", 1234)


@getCode.post("/", dependencies=[Depends(RateLimiter(times=1, seconds=5))])
async def auth_request(user: CodeRequest):
    user_dict = user.dict()
    if not await user_exist(user_dict["email"]):
        await insert_user(user_dict)
    code = random.randint(1000, 9999)
    await send_code(user_dict["email"], code)
    await setAuthCode(user_dict["email"], code)
    return {"message": "Please check email!"}


@getCode.post("/check", dependencies=[Depends(RateLimiter(times=1, seconds=2))])
async def auth_check(code: CodeModel):
    user_dict = code.dict()
    _code = user_dict["code"]
    email = user_dict["email"]

    if not await user_exist(email):
        return HTTPException(status_code=404, detail="User not exist")

    user = await get_user(email)
    if int(_code) == int(user["auth_code"]):
        await setAuthCode(user_dict["email"], 0)

        jwt_token = jwt.encode({
            "email": email,
            "expires_in": int((datetime.datetime.now() + datetime.timedelta(days=7)).timestamp())
        }, "SECRET", algorithm="HS256")
        return {"message": "code valid!", "token": jwt_token}

    return HTTPException(status_code=401, detail="Not valid code")


