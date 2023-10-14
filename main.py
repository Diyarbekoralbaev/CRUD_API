from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from functions import *

app = FastAPI(
    title="Diyarbek's API",
    description="Simple CRUD API for portfolio",
    root_path="/",
    docs_url="/api/docs",
)



@app.get("/")
def read_root():
    return {"creator": "Diyarbek Oralbaev", "version": "1.0"}



@app.get("/info")
async def get_infos():
    info = await get_info()
    json = {}
    for i in info:
        json[i[0]] = {
            "name": i[1],
            "phone": i[2],
            "email": i[3],
            "address": i[4],
            "birthday": i[5]
        }
    return json

@app.post("/info")
async def add_info(info: Info):
    return await insert_info(info)

@app.put("/info")
async def put_infos(id: int, info: Info):
    return await update_info(info)

@app.delete("/info")
async def delete_infos(id : int):
    return await delete_info(id)



@app.get("/portfolio")
async def get_portfolios():
    portfolio = await get_portfolio()
    json = {}
    for i in portfolio:
        json[i[0]] = {
            "title": i[1],
            "description": i[2],
            "image": i[3]
        }
    return json

@app.post("/portfolio")
async def add_portfolio(portfolio: Portfolio):
    return await insert_portfolio(portfolio)

@app.put("/portfolio")
async def update_portfolios(id : int, portfolio: Portfolio):
    return await update_portfolio(id, portfolio)

@app.delete("/portfolio")
async def delete_portfolios(id : int):
    return await delete_portfolio(id)



@app.get("/messages")
async def get_messagess():
    message = await get_messages()
    json = {}
    for i in message:
        json[i[0]] = {
            "name": i[1],
            "phone": i[2],
            "email": i[3],
            "message": i[4]
        }

@app.post("/messages")
async def send_message(message: Message):
    return await send_message(message)

@app.delete("/messages")
async def delete_messages(id : int):
    return await delete_message(id)



if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)