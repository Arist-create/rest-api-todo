from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse
from src.data.registration_data_access import registration_data_access
from src.data.database.table_models.user_table_model import UserTableModel


async def registration_ctrl(db: AsyncSession, user: UserTableModel) -> JSONResponse:
    response = await registration_data_access(db, user)
    if response is None:
        return JSONResponse(status_code=400, content={"DuplicateUsernameError": "Username already exists"})
    return JSONResponse(status_code=201, content={"message": "User created successfully"})
