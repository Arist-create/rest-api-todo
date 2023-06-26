from fastapi import APIRouter, Body, Depends
import http
from src.controllers.registration_ctrl import registration_ctrl
from src.data.database.main_db import get_db
from src.schemas.registration_schemas import RegistrationRequestSchema, RegistrationResponseSchema
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/registration",
             summary="Регистрация",
             status_code=http.HTTPStatus.CREATED,
             response_model=RegistrationResponseSchema
             )
async def registration_route(user: RegistrationRequestSchema = Body(),
                             db: AsyncSession = Depends(get_db)) -> JSONResponse:
    return await registration_ctrl(db, user)
