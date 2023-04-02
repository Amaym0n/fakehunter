from fastapi import APIRouter

from api_routes.route_users import users_router


api_router = APIRouter()
api_router.include_router(router=users_router)
