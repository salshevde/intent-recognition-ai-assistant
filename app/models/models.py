from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime
from enum import Enum

class User(BaseModel):
    username: str
    password: str
    
class UserInput(BaseModel):
    text : str
    user_id : Optional[str] = "anonymous"

class Response(BaseModel):
    intent : str
    confidence : float
    response : str
    entities: Optional[Dict[str,str]] = None

class Chat(BaseModel):
    user_id : str
    input_text: str
    response: Response
    timestamp: datetime
    entities: Optional[Dict[str,str]] = None


