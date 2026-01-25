from fastapi import FastAPI, Response, status, Depends, APIRouter, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. import database, models, schemas, utils, oauth2
from sqlalchemy.orm import Session
from sqlalchemy import select

router=APIRouter(tags=["Authentication"])

@router.post("/login")
def get_login(user_credentials: OAuth2PasswordRequestForm=Depends(), db: Session=Depends(database.get_db)):
    stmt=select(models.User).where(models.User.email==user_credentials.username)
    user=db.execute(stmt).scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
    
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")

    # create a token and return
    access_token=oauth2.create_access_token(data={"user_id":user.id})


    return {"access_token":access_token, "token_type":"bearer"}