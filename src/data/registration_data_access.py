from src.data.database.table_models.user_table_model import UserTableModel
from sqlalchemy.ext.asyncio import AsyncSession


async def registration_data_access(db: AsyncSession, user: UserTableModel) -> dict:
    new_user = UserTableModel(
        username=getattr(user, "username"),
        password=getattr(user, "password"),
        is_superuser=False
    )
    try:
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        return await new_user.as_dict()
    except Exception:
        return None
