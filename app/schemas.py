from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    password: str
    


class UserCreate(UserBase):
    name: str
    position: str
    skills: str


class User(UserCreate):

    class Config:
        orm_mode = True