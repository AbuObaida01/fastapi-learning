from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app=FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool=True
    rating: Optional[int]=None

# we will create a memory to hold our posts because we are not using any database
my_posts=[{"title": "first title", "content": "first content", "id": 1},
          {"title": "second title", "content": "second content", "id": 2}]

@app.get("/posts")
async def get_posts():
    return{"data": my_posts}
@app.post("/posts")
async def create_posts(post: Post):
    print(post.title)
    print(post.content)
    print(post.published)
    print(post.rating)
    print(post.dict())
    return post