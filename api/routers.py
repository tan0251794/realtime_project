from fastapi import APIRouter

from api.endpoints import user
from library.constant.setting import USER_PREFIX

api_router = APIRouter()

# include some routes
api_router.include_router(user.router, tags=["users"], prefix=USER_PREFIX)
