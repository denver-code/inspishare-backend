from app.v1.api.database_api import *


async def user_exist(email):
    return bool(await find_one_query("users", {"email": email}))


async def insert_user(user_object):
    return bool(await users.insert_one({
        "email": user_object["email"],
        "services": [],
        "name": "",
        "personal_link": "",
        "auth_code": 0,
        "delete_code": 0
    }))


async def insert_service(email, _service):
    """
    service - {
    "name": "Telegram",
    "description": "Telegram — кроссплатформенная система мгновенного обмена сообщениями.",
    "url": "https://t.me/idenver_bot",
    "username": "idenver_bot"
    }
    """
    user = await get_user(email)
    for service in user["services"]:
        if service["username"] == _service["username"] \
                and service["name"].lower() == _service["name"].lower():
            return "Service already exist on your account!"


async def setAuthCode(email, code):
    user = await get_user(email)
    print(user)
    user["auth_code"] = code
    await update_db("users", {"email": email}, user)


async def get_user(email):
    return await find_one_query("users", {"email": email})


async def delete_user(email):
    return bool(await users.delete_one({"email": email}))
