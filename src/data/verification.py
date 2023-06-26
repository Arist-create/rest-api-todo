from src.data.database.table_models.user_table_model import UserTableModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


async def verify_user(db: AsyncSession, user: UserTableModel) -> dict | None:
    result = await db.execute(
        select(UserTableModel).filter(
            UserTableModel.username == user.username,
            UserTableModel.password == user.password
        )
    )
    try:
        user = result.scalars().one()
        return await user.as_dict()
    except Exception:
        return None
