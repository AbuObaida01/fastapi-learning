from fastapi import FastAPI, Response, status, Depends, APIRouter, HTTPException
from .. import database, models, schemas, utils
from sqlalchemy.orm import Session
from sqlalchemy import select

router=APIRouter(tags=["Authentication"])

@router.post("/login")
def get_login(user_credentials: schemas.UserLogin, db: Session=Depends(database.get_db)):
    stmt=select(models.User).where(models.User.email==user_credentials.email)
    user=db.execute(stmt).scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")

    # ROuter

    return {"message": "Successfully logged in"}