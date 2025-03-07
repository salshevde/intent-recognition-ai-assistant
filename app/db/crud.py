from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime
from typing import Optional, Dict
from ..core.config import settings
from ..models.models import UserInput, Chat, Response,User
from bson import ObjectId

client = AsyncIOMotorClient(settings.DATABASE_URL)
db = client[settings.DATABASE_NAME]


async def create_user(user: User)->dict:

    if await db.users.find_one({"username":user.username}):
        raise ValueError("Username already taken")

    new_user = user.dict()

    result = await db.users.insert_one(new_user)
    return{
        "username":user.username,
        "user_id": str(result.inserted_id)
    }
    
async def login_user(user: User)->Optional[dict]:

    if user:= await db.users.find_one({"username":user.username, "password":user.password}):
        return{
            "username":user["username"],
            "user_id": str(user["_id"])
        }
    return None
async def find_user(user_id:str)->Optional[dict]:

    if user:= await db.users.find_one({"_id":user_id}):
        return{
            "username":user["username"]
        }
    return None
async def store_chat(user_input: UserInput, response: Response):

    chat = Chat(
        username = user_input.username,
        input_text = user_input.text,
        response = response,
        timestamp=datetime.utcnow(),

    )
    await db.chats.insert_one(chat.dict())
    return chat

async def get_user_chats(username: str , limit:int=100):
    query = {"username": username}
    found_user = await db.users.find_one({"username": username})
    if not found_user:
        raise ValueError("User not found")

    cursor = db.chats.find(query).sort("timestamp", -1).limit(limit)
    chats = await cursor.to_list(length=limit)
    return [Chat(**chat) for chat in chats]

 