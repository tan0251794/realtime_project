from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from api.user.schemas import UserSchema
from library.database import SessionLocal
# models.Base.metadata.create_all(bind=engine)
from models.user.model import User

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/users/", response_model=List[UserSchema])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users


@app.get("/")
async def root():
    return {"message": "Hello World"}
