import http
from fastapi import APIRouter, Body, Depends
from src.controllers.authorization_ctrl import get_user_from_token
from src.schemas.user_schemas import UserRequestSchema
from src.controllers.user_ctrl import UserController
from src.data.database.main_db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/users",
             summary="Создать пользователя",
             status_code=http.HTTPStatus.CREATED,
             )
async def create_user_route(data: UserRequestSchema = Body(),
                            db: AsyncSession = Depends(get_db),
                            superuser: dict = Depends(get_user_from_token)) -> JSONResponse:
    return await UserController.create_user(db, data, superuser)


@router.delete("/users/{user_id}",
               summary="Удалить пользователя",
               status_code=http.HTTPStatus.OK,
               )
async def delete_user_route(user_id: str,
                            db: AsyncSession = Depends(get_db),
                            superuser: dict = Depends(get_user_from_token)) -> JSONResponse:
    return await UserController.delete_user(db, user_id, superuser)
