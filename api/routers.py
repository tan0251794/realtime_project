from fastapi import APIRouter

from api.endpoints import data_source_api, user
from library.constant.setting import USER_PREFIX

api_router = APIRouter()

# include some routes
api_router.include_router(user.router, tags=["users"], prefix=USER_PREFIX)
api_router.include_router(data_source_api.router, tags=["data_source_apis"], prefix='/data_source_apis')
