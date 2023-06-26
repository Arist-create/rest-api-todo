from fastapi import APIRouter, Body, Depends
import http
from src.controllers.authorization_ctrl import get_user_from_token
from src.controllers.task_ctrl import TaskController
from src.data.database.main_db import get_db
from src.schemas.task_schemas import TaskRequestSchema, TaskResponseSchema
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/tasks",
             summary="Создать задачу",
             status_code=http.HTTPStatus.CREATED,
             response_model=TaskResponseSchema
             )
async def create_task_route(db: AsyncSession=Depends(get_db), 
                            data: TaskRequestSchema=Body(), 
                            user=Depends(get_user_from_token)) -> JSONResponse:
    return await TaskController.create_task(db, data, user)


@router.get("/tasks",
            summary="Получить список задач",
            status_code=http.HTTPStatus.OK,
            response_model=list[TaskResponseSchema]
            )
async def get_tasks_route(db: AsyncSession=Depends(get_db), 
                          user: dict=Depends(get_user_from_token)) -> JSONResponse:
    return await TaskController.get_tasks(db, user)


@router.get("/tasks/{task_id}",
            summary="Получить задачу",
            status_code=http.HTTPStatus.OK,
            response_model=TaskResponseSchema
            )
async def get_task_route(task_id: str, 
                         db: AsyncSession=Depends(get_db), 
                         user: dict=Depends(get_user_from_token)) -> JSONResponse:
    return await TaskController.get_task(db, task_id, user)


@router.patch("/tasks/{task_id}",
            summary="Изменить задачу",
            status_code=http.HTTPStatus.OK,
            response_model=TaskResponseSchema
            )
async def edit_task_route(task_id: str, 
                          db: AsyncSession=Depends(get_db), 
                          data: TaskRequestSchema=Body(), 
                          user: dict=Depends(get_user_from_token)) -> JSONResponse:
    return await TaskController.edit_task(db, task_id, data, user)


@router.delete("/tasks/{task_id}",
            summary="Удалить задачу",
            status_code=http.HTTPStatus.OK
            )
async def delete_task_route(task_id: str, 
                            db: AsyncSession=Depends(get_db), 
                            user: dict=Depends(get_user_from_token)) -> JSONResponse:
    return await TaskController.delete_task(db, task_id, user)