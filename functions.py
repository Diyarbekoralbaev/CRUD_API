import psycopg2
from psycopg2 import sql
from pydantic import BaseModel

connection = psycopg2.connect(
            user="postgres",
            password="PASSWORD",
            host="localhost",
            port="5432",
            database="DATABASE_NAME"
)

connection.autocommit = True

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS myinfo (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        phone VARCHAR(255),
        email VARCHAR(255),
        address VARCHAR(255),
        birthday VARCHAR(255)
    )""")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS portfolio (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255),
        description VARCHAR(255),
        image VARCHAR(255)
    )""")



cursor.execute("""
    CREATE TABLE IF NOT EXISTS contact (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        phone VARCHAR(255),
        email VARCHAR(255),
        message VARCHAR(500)
    )""")

class Info(BaseModel):
    name: str
    phone: str
    email: str
    address: str
    birthday: str

class Portfolio(BaseModel):
    title: str
    description: str
    image: str

class Message(BaseModel):
    name: str
    phone: str
    email: str
    message: str


async def get_info():
    try:
        cursor.execute("SELECT * FROM myinfo")
        return cursor.fetchall()
    except Exception as e:
        return {"status": "error", "error_message": e}

async def insert_info(info: Info):
    try:
        cursor.execute("INSERT INTO myinfo (name, phone, email, address, birthday) VALUES (%s, %s, %s, %s, %s)",
                       (info.name, info.phone, info.email, info.address, info.birthday))
        return {"status": "success"}
    except Exception as e:
        print(e)  
        return {"status": "error", "error_message": str(e)}
    
async def update_info(info: Info):
    try:
        cursor.execute("UPDATE myinfo SET name=%s, phone=%s, email=%s, address=%s, birthday=%s", (info.name, info.phone, info.email, info.address, info.birthday))
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "error_message": str(e)}

async def delete_info(id : int):
    try:
        cursor.execute("DELETE FROM myinfo WHERE id=%s", (id,))
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "error_message": str(e)}



async def get_portfolio():
    try:
        cursor.execute("SELECT * FROM portfolio")
        return cursor.fetchall()
    except Exception as e:
        return {"status": "error", "error_message": str(e)}

async def insert_portfolio(portfolio: Portfolio):
    try:
        cursor.execute("INSERT INTO portfolio (title, description, image) VALUES (%s, %s, %s)", (portfolio.title, portfolio.description, portfolio.image))
        return {"status": "success"}
    except Exception as e:
        print(e)  # Add this line to print the error
        return {"status": "error", "error_message": str(e)}

async def update_portfolio(id : int,portfolio: Portfolio):
    try:
        cursor.execute("UPDATE portfolio SET title=%s, description=%s, image=%s WHERE id=%s", (portfolio.title, portfolio.description, portfolio.image, id))
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "error_message": str(e)}

async def delete_portfolio(id : int):
    try:
        cursor.execute("DELETE FROM portfolio WHERE id=%s", (id,))
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "error_message": str(e)}
    


async def send_message(message: Message):
    try:
        cursor.execute("INSERT INTO contact (name, phone, email, message) VALUES (%s, %s, %s, %s)", (message.name, message.phone, message.email, message.message))
        return {"status": "success"}
    except Exception as e:
        print(e)  # Add this line to print the error
        return {"status": "error", "error_message": str(e)}

async def get_messages():
    try:
        cursor.execute("SELECT * FROM contact")
        return cursor.fetchall()
    except Exception as e:
        return {"status": "error", "error_message": str(e)}

async def delete_message(id : int):
    try:
        cursor.execute("DELETE FROM contact WHERE id=%s", (id,))
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "error_message": str(e)}
    
if __name__ == "__main__":
    connection.close()