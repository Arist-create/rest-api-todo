from pydantic import BaseModel


class TaskRequestSchema(BaseModel):
    title: str = 'title'
    description: str = 'description'


class TaskResponseSchema(BaseModel):
    task_id: int = 1
    user_id: int = 2
    title: str = 'title'
    description: str = 'description'
