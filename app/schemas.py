from pydantic import BaseModel, Json
from typing import Any

class UserBase(BaseModel):
    email: str
    password: str
    


class UserCreate(UserBase):
    name: str
    position: str
    skills: Any


class User(UserCreate):

    class Config:
        orm_mode = True