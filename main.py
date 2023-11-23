from typing import Union
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def root_action():
    return {"surname": "Балаев", "name": "Кирилл", "patronymic": "Гурамович"}

@app.get("/users")
def users_action():
    return {"phone_number": "89131171847", "email": "kirillbalaev568@gmail.com"}

@app.get("/tools")
def users_action():
    return {"info": "Смог сделать простое API, используя FastAPI"}