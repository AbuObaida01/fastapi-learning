from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import select
from .. import schemas, oauth2, database, models
router=APIRouter(
    prefix="/votes",
    tags=["VOTES"]
)
@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session=Depends(database.get_db), current_user:int =Depends(oauth2.get_current_user)):
    stmt=select(models.Post).where(models.Post.id==vote.post_id)
    post=db.execute(stmt).scalar_one_or_none()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {vote.post_id} does not exist")
    stmt1=select(models.Votes).where(models.Votes.post_id==vote.post_id, models.Votes.user_id==current_user.id)
    found_vote=db.execute(stmt1).scalar_one_or_none()
    if(vote.dir==1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"user{current_user.id} has already voted on post {vote.post_id}")
        new_vote=models.Votes(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return{"message":"successfull"}
    
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="already voted")
        db.delete(found_vote)
        db.commit()
        return{"message": "successfully delete vote"}