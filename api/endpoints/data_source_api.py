from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from dependences.authentication import basic_auth
from library.database import get_db
from models.data_source_api import DataSourceAPI
from models.schemas.user import UserSchema

router = APIRouter()


@router.get(
    path="/",
    name="List DSA",
    description='Danh sách DSA',
    status_code=status.HTTP_200_OK,
    response_model=List[UserSchema]
)
async def list_dsa(basic_auth: str = Depends(basic_auth), db: Session = Depends(get_db)):
    print(1)
    dsa_list = db.query(DataSourceAPI).all()
    print(dsa_list)
    return dsa_list


# @router.post(
#     path="/",
#     name="Create DSA",
#     description='Tạo DSA',
#     status_code=status.HTTP_200_OK,
#     response_model=List[UserSchema]
# )
# async def create(basic_auth: str = Depends(basic_auth), db: Session = Depends(get_db)):
#     dsa = DataSourceAPI(
#
#     )
#     return dsa_list
