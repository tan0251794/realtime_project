from typing import List

from fastapi import Depends, FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from api.user.schemas import UserSchema
from library.database import SessionLocal, engine
from library.socket_service import html_template
from models.user.model import Base, User

Base.metadata.create_all(bind=engine)

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


@app.get("/socket/")
async def get():
    return HTMLResponse(html_template)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
