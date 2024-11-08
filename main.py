from fastapi import FastAPI
from routes import users

app = FastAPI()


app.include_router(users.route)


@app.get("/")
async def main():
    return {"message": "working"}
