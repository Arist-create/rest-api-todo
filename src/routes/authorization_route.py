from fastapi import APIRouter, Depends
import http
from fastapi.security import OAuth2PasswordRequestForm
from src.controllers.authorization_ctrl import authorization_ctrl
from src.data.database.main_db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse
from src.schemas.authorization_schemas import AuthorizationResponseSchema

router = APIRouter()


@router.post("/authorization",
             summary="Авторизация",
             status_code=http.HTTPStatus.CREATED,
             response_model=AuthorizationResponseSchema
             )
async def authorization_route(form_data: OAuth2PasswordRequestForm = Depends(),
                              db: AsyncSession = Depends(get_db)) -> JSONResponse:
    return await authorization_ctrl(db, form_data)
