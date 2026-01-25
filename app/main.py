from fastapi import FastAPI, Response, status, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional, List
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy import select
from sqlalchemy.orm import Session
from . import models,schemas, utils
from .database import engine, SessionLocal, get_db
from .router import user,post,auth

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

#Coonectiong to the database
while True:
    try:
        conn=psycopg2.connect(host='localhost', database='fastapi',port=5433, user='postgres', password='arshiFatima1998@.', cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print("Database connected")
        break
    except Exception as error:
        print("failed")
        print("Error", error)
        time.sleep(2)

# we will create a memory to hold our posts because we are not using any database
# my_posts=[{"title": "first title", "content": "first content", "id": 1},
#           {"title": "second title", "content": "second content", "id": 2}]

# def del_post(id: int):
#     for i, p in enumerate(my_posts):
#         if p['id']==id:
#             return i

app.include_router(user.router)
app.include_router(post.router)
app.include_router(auth.router)