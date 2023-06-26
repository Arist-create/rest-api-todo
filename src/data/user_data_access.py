from src.data.database.table_models.user_table_model import UserTableModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class UserDataAccess:
    async def create_user(db: AsyncSession, user: UserTableModel) -> dict | None:
        new_user = UserTableModel(
            username=getattr(user, "username"),
            password=getattr(user, "password"),
            is_superuser=getattr(user, "is_superuser")
        )
        try:
            db.add(new_user)
            await db.commit()
            await db.refresh(new_user)
            return await new_user.as_dict()
        except Exception:
            return None

    async def delete_user(db: AsyncSession, user_id: str) -> bool | None:
        result = await db.execute(
            select(UserTableModel).filter(
                UserTableModel.user_id == int(user_id)
            )
        )
        try:
            deleted_task = result.scalars().one()
            await db.delete(deleted_task)
            await db.commit()
            return True
        except Exception:
            return None
