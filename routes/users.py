from fastapi import APIRouter

route = APIRouter()


@route.get("/users")
async def users():
    return ["this is a list of users"]
