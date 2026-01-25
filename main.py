from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app=FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool=True
    rating: Optional[int]=None


@app.get("/")
async def root():
    return{"message":"Hello World !!!"}

@app.get("/posts")
async def get_posts():
    return{"data":"This is your posts"} 

@app.post("/posts")
async def create_posts(post: Post):
    print(post.title) 
    print(post.content)
    print(post.published)
    print(post.rating)
    print(post.dict())
    return post
    # return{"message":post}