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
async def store_chat(user_input: UserInput, response: Response):

    chat = Chat(
        user_id = user_input.user_id,
        input_text = user_input.text,
        response = response,
        timestamp=datetime.utcnow(),

    )
    await db.chats.insert_one(chat.dict())
    return chat

async def get_user_chats(user_id: str , limit:int=100):
    cursor = db.chats.find({"user_id":user_id}).sort("timestamp",-1).limit(limit)
    chats = await cursor.to_list(length=limit)
    return [Chat(**chat) for chat in chats]