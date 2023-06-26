from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse
from src.data.user_data_access import UserDataAccess
from src.data.database.table_models.user_table_model import UserTableModel


class UserController:
    async def create_user(db: AsyncSession, user: UserTableModel, superuser: dict) -> JSONResponse:
        if superuser["is_superuser"] is False:
            return JSONResponse(status_code=403, content={"InsufficientPermissionsError": "Only admin can create users"})
        response = await UserDataAccess.create_user(db, user)
        if response is None:
            return JSONResponse(status_code=400, content={"message": "Username already exists"})
        return JSONResponse(status_code=201, content={"message": "User created successfully"})

    async def delete_user(db: AsyncSession, user_id: str, superuser: dict) -> JSONResponse:
        if superuser["is_superuser"] is False:
            return JSONResponse(status_code=403, content={"InsufficientPermissionsError": "Only admin can delete users"})
        response = await UserDataAccess.delete_user(db, user_id)
        if response is None:
            return JSONResponse(status_code=404, content={"NotFoundError": "User not found"})
        return JSONResponse(status_code=200, content={"message": "User deleted successfully"})
