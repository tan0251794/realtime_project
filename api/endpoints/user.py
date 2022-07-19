import secrets
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from starlette import status

from library.database import get_db
from models.schemas.user import UserSchema

# from models.user import User

router = APIRouter()

security = HTTPBasic()


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "tanlc")
    correct_password = secrets.compare_digest(credentials.password, "123456")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@router.get("/me")
async def read_current_user(username: str = Depends(get_current_username)):
    return {"username": username}


# @router.get(
#     path="/",
#     name="List User",
#     description='Danh sách người dùng',
#     # responses=open_api_standard_responses(success_status_code=HTTP_201_CREATED,
#     #                                       success_response_model=ItemUploadFileResponseSchema,
#     #                                       fail_response_model=FailResponse),
#     status_code=status.HTTP_200_OK,
#     response_model=List[UserSchema]
# )
# async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = db.query(User).offset(skip).limit(limit).all()
#     return users
