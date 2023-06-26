from sqlalchemy import select
from src.data.database.table_models.task_table_model import TaskTableModel
from sqlalchemy.ext.asyncio import AsyncSession


class TaskDataAccess:
    async def create_task(db: AsyncSession, task: TaskTableModel, user: dict) -> dict:
        created_task = TaskTableModel(
            user_id=user["user_id"],
            title=getattr(task, "title"),
            description=getattr(task, "description")
        )
        db.add(created_task)
        await db.commit()
        await db.refresh(created_task)
        return await created_task.as_dict()

    async def get_task(db: AsyncSession, task_id: str, user: dict) -> dict | None:
        result = await db.execute(
            select(TaskTableModel).filter(
                TaskTableModel.task_id == int(task_id),
                TaskTableModel.user_id == int(user["user_id"])
            )
        )
        try:
            task = result.scalars().one()
            return await task.as_dict()
        except Exception:
            return None

    async def get_tasks(db: AsyncSession, user: dict) -> list:
        result = await db.execute(
            select(TaskTableModel).filter(
                TaskTableModel.user_id == int(user["user_id"]),
            )
        )
        arr = []
        try:
            task = result.scalars().all()
            for i in task:
                arr.append(await i.as_dict())
        except Exception:
            pass
        return arr

    async def edit_task(db: AsyncSession, task_id: str, task: TaskTableModel, user: dict) -> dict | None:
        result = await db.execute(
            select(TaskTableModel).filter(
                TaskTableModel.task_id == int(task_id),
                TaskTableModel.user_id == int(user["user_id"])
            )
        )
        try:
            updated_task = result.scalars().one()
            updated_task.title = task.title
            updated_task.description = task.description
            await db.commit()
            await db.refresh(updated_task)
            return await updated_task.as_dict()
        except Exception:
            return None

    async def delete_task(db: AsyncSession, task_id: str, user: dict) -> bool | None:
        result = await db.execute(
            select(TaskTableModel).filter(
                TaskTableModel.task_id == int(task_id),
                TaskTableModel.user_id == int(user["user_id"])
            )
        )
        try:
            deleted_task = result.scalars().one()
            await db.delete(deleted_task)
            await db.commit()
            return True
        except Exception:
            return None
