from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from typing import Optional
from random import randrange

app=FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool=True
    rating: Optional[int]=None

# we will create a memory to hold our posts because we are not using any database
my_posts=[{"title": "first title", "content": "first content", "id": 1},
          {"title": "second title", "content": "second content", "id": 2}]

def del_post(id: int):
    for i, p in enumerate(my_posts):
        if p['id']==id:
            return i

@app.get("/posts")
async def get_posts():
    return{"data": my_posts}

# TO create posts
@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_posts(post: Post):
    post_dict=post.dict()
    post_dict['id']=randrange(0,10000)
    my_posts.append(post_dict)
    return post_dict


## to retrive latest post 
# @app.get("/posts/latest")
# async def get_latest():
#     post=my_posts[-1]
#     return post

# To retrive any specific post by id
@app.get("/posts/{id}")
async def get_post(id: int):
    print(id)
    for post in my_posts:
        if post['id']==id:
            return{"post_detail": post}

    # We can also use HTTP Exception
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {id} not founnd")




## using here will give wrror because it comes after another posts/{id} which will take latest also as id
# ## to retrive latest post 
# @app.get("/posts/latest")
# async def get_latest():
#     post=my_posts[-1]
#     return post


# to delete a post
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id:int):
    index=del_post(id)
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {id} not found")
    my_posts.pop(index)

# to update a post
@app.patch("/posts/{id}")
async def update_post(id:int, post:Post):
    index=del_post(id)
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {id} not found")
    post_dict=post.dict()
    post_dict['id']=id
    my_posts[index]=post_dict
    return{"post_detail":post_dict}