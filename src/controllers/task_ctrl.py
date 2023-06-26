from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse
from src.data.task_data_access import TaskDataAccess
from src.data.database.table_models.task_table_model import TaskTableModel


class TaskController:
    async def create_task(db: AsyncSession, task: TaskTableModel, user: dict) -> JSONResponse:
        response = await TaskDataAccess.create_task(db, task, user)
        return JSONResponse(status_code=201, content=response)

    async def get_task(db: AsyncSession, task_id: str, user: dict) -> JSONResponse:
        response = await TaskDataAccess.get_task(db, task_id, user)
        if response is None:
            return JSONResponse(status_code=404, content={"NotFoundError": "Task not found"})
        return JSONResponse(status_code=200, content=response)

    async def get_tasks(db: AsyncSession, user: dict) -> JSONResponse:
        response = await TaskDataAccess.get_tasks(db, user)
        return JSONResponse(status_code=200, content=response)

    async def edit_task(db: AsyncSession, task_id: str, task: TaskTableModel, user: dict) -> JSONResponse:
        response = await TaskDataAccess.edit_task(db, task_id, task, user)
        if response is None:
            return JSONResponse(status_code=404, content={"NotFoundError": "Task not found"})
        return JSONResponse(status_code=200, content=response)

    async def delete_task(db: AsyncSession, task_id: str, user: dict) -> JSONResponse:
        response = await TaskDataAccess.delete_task(db, task_id, user)
        if response is None:
            return JSONResponse(status_code=404, content={"NotFoundError": "Task not found"})
        return JSONResponse(status_code=200, content={"message": "Task deleted successfully"})
