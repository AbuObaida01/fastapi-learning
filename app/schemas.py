from pydantic import BaseModel, EmailStr
from datetime import datetime
from pydantic import ConfigDict

class PostBase(BaseModel):
    title: str
    content: str
    # published: bool=True

class PostCreate(PostBase):
    pass

class ResponsePost(PostBase):
    # created_at: datetime
    id: int

    model_config=ConfigDict(from_attributes=True)

    # class Config:
    #     orm_mode=True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    model_config=ConfigDict(from_attributes=True)

class UserLogin(BaseModel):
    email: EmailStr
    password: str