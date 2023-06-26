from src.data.database.main_db import init_db, engine
from fastapi import FastAPI
from src.routes import registration_route, authorization_route, user_routes, task_routes
from src.data.user_data_access import UserDataAccess
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.data.database.table_models.user_table_model import UserTableModel


app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await init_db()
    db = AsyncSession(engine, expire_on_commit=False)
    await UserDataAccess.create_user(db, UserTableModel(username="admin", password="admin", is_superuser=True))
    await db.close()


app.include_router(registration_route.router)
app.include_router(authorization_route.router)
app.include_router(user_routes.router, tags=["Users"])
app.include_router(task_routes.router, tags=["Tasks"])
