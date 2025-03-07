from fastapi import APIRouter, HTTPException, Depends
from typing import List, Annotated
import logging
from ..models.models import Response, UserInput, Chat,User
from ..services.intent_recognition import recognize_intent
from ..db.crud import create_user,find_user,login_user,store_chat,get_user_chats


router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/")
async def home():
    try:
        return {
            "message":"Welcome to Intent Recognition system!!!"
        }
    except ValueError as e:
        raise HTTPException(status_code=500,detail=str(e))

@router.post("/register")
async def create_new_user(user: User):
    try:
        return await create_user(user)
    except ValueError as e:
        raise HTTPException(status_code=500,detail=str(e))

@router.post("/login")
async def login(user: User):
    if user_data := await login_user(user):
        return user_data
    raise HTTPException(status_code=500,detail=f"Invalid username or password")


@router.post('/process',response_model=Response)
async def process_input(user_input: UserInput):
    try:
        logger.info(f"Processing input for user: {user_input.username}")

        intent = await recognize_intent(user_input.text, user_input.username)

        await store_chat(
            user_input=user_input,
            response=intent
        )
        return intent

    except Exception as e:
        except_str = "Error processing input"
        logger.error(f"{except_str}: {str(e)}",exc_info=True)
        raise HTTPException(status_code=500,detail=f"{except_str}")

@router.post('/chat/{username}',response_model=List[Chat])
async def user_chats(username: str):
    try:
        return await get_user_chats(username)
    except Exception as e:
        except_str = "Error fetching chat"
        logger.error(f"{except_str}: {str(e)}",exc_info=True)
        raise HTTPException(status_code=404,detail=f"{except_str}")#FIXME
        




