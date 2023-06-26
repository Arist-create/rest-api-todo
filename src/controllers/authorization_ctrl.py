from fastapi.security.oauth2 import OAuth2PasswordBearer
from fastapi import Depends
from src.data.verification import verify_user
from fastapi.responses import JSONResponse
from datetime import datetime, timedelta
import jwt
import os
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm

SECRET_KEY = os.getenv("SECRET_KEY")

ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/authorization")


async def authorization_ctrl(db: AsyncSession, user: OAuth2PasswordRequestForm) -> JSONResponse:
    response = await verify_user(db, user)
    if response is None:
        return JSONResponse(status_code=400, content={"InvalidCredentialsError": "Wrong username or password"})
    to_encode = response.copy()
    access_token_expires = timedelta(minutes=30)
    expire = datetime.utcnow() + access_token_expires
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return JSONResponse(status_code=201, content={"access_token": encoded_jwt, "token_type": "bearer"})


async def get_user_from_token(token: str = Depends(oauth2_scheme)) -> dict:
    user = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return user
