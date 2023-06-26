import json
from src.data.database.main_db import init_db
from sqlalchemy.ext.asyncio import AsyncSession
from src.data.database.table_models.user_table_model import UserTableModel
from src.data.database.main_db import engine
from src.data.user_data_access import UserDataAccess


async def test_registration(test_app):
    await init_db()
    db = AsyncSession(engine, expire_on_commit=False)
    response = await UserDataAccess.create_user(db, UserTableModel(username="admin", password="admin", is_superuser=True))
    await db.close()
    content = {
        "username": "ivan2002",
        "password": 12345
    }
    result = {"message": "User created successfully"}
    response = await test_app.post("/registration", content=json.dumps(content))

    assert response.status_code == 201
    assert response.json() == result


async def test_registration_invalid_data(test_app):
    content = {
        "username": "ivan2002",
        "password": "12345"
    }
    result = {"DuplicateUsernameError": "Username already exists"}
    response = await test_app.post("/registration", content=json.dumps(content))

    assert response.status_code == 400
    assert response.json() == result


async def test_authorization(test_app):
    content = {"username": "ivan2002",
               "password": "12345", "grant_type": "password"}
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = await test_app.post("/authorization", data=content, headers=headers)
    global token_user
    token_user = response.json()["access_token"]
    print(token_user)
    assert response.status_code == 201


async def test_authorization_invalid_data(test_app):
    content = {"username": "ivan2002",
               "password": "123", "grant_type": "password"}
    result = {"InvalidCredentialsError": "Wrong username or password"}
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = await test_app.post("/authorization", data=content, headers=headers)

    assert response.status_code == 400
    assert response.json() == result


async def test_create_task(test_app):
    content = {
        "title": "test",
        "description": "test task"
    }
    result = {"task_id": 1,
              "user_id": 2,
              "title": "test",
              "description": "test task"}
    headers = {'Authorization': f'Bearer {token_user}'}
    response = await test_app.post("/tasks", content=json.dumps(content), headers=headers)
    assert response.status_code == 201
    assert response.json() == result


async def test_get_task_invalid_data(test_app):
    result = {"NotFoundError": "Task not found"}
    headers = {'Authorization': f'Bearer {token_user}'}
    response = await test_app.get("/tasks/2", headers=headers)
    assert response.status_code == 404
    assert response.json() == result


async def test_get_tasks(test_app):
    result = [{"task_id": 1,
              "user_id": 2,
               "title": "test",
               "description": "test task"}]
    headers = {'Authorization': f'Bearer {token_user}'}
    response = await test_app.get("/tasks", headers=headers)
    assert response.status_code == 200
    assert response.json() == result


async def test_edit_task(test_app):
    content = {"title": "test edit",
               "description": "test edit task"}
    result = {"task_id": 1,
              "user_id": 2,
              "title": "test edit",
              "description": "test edit task"}
    headers = {'Authorization': f'Bearer {token_user}'}
    response = await test_app.patch("/tasks/1", content=json.dumps(content), headers=headers)
    assert response.status_code == 200
    assert response.json() == result


async def test_edit_task_invalid_data(test_app):
    content = {"title": "test edit",
               "description": "test edit task"}
    result = {"NotFoundError": "Task not found"}
    headers = {'Authorization': f'Bearer {token_user}'}
    response = await test_app.patch("/tasks/2", content=json.dumps(content), headers=headers)
    assert response.status_code == 404
    assert response.json() == result


async def test_delete_task(test_app):
    result = {"message": "Task deleted successfully"}
    headers = {'Authorization': f'Bearer {token_user}'}
    response = await test_app.delete("/tasks/1", headers=headers)
    assert response.status_code == 200
    assert response.json() == result


async def test_delete_task_invalid_data(test_app):
    result = {"NotFoundError": "Task not found"}
    headers = {'Authorization': f'Bearer {token_user}'}
    response = await test_app.delete("/tasks/2", headers=headers)
    assert response.status_code == 404
    assert response.json() == result


async def test_authorization_admin(test_app):
    content = {"username": "admin",
               "password": "admin", "grant_type": "password"}
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = await test_app.post("/authorization", data=content, headers=headers)
    global token_admin
    token_admin = response.json()["access_token"]

    assert response.status_code == 201


async def test_create_user_no_permissions(test_app):
    content = {
        "username": "test username",
        "password": "test password",
        "is_superuser": True
    }
    result = {"InsufficientPermissionsError": "Only admin can create users"}
    headers = {'Authorization': f'Bearer {token_user}'}
    response = await test_app.post(f"/users", content=json.dumps(content), headers=headers)
    assert response.status_code == 403
    assert response.json() == result


async def test_create_user(test_app):
    content = {
        "username": "test username",
        "password": "test password",
        "is_superuser": True
    }
    result = {"message": "User created successfully"}
    headers = {'Authorization': f'Bearer {token_admin}'}
    response = await test_app.post(f"/users", content=json.dumps(content), headers=headers)
    assert response.status_code == 201
    assert response.json() == result


async def test_delete_user_no_permissions(test_app):
    result = {"InsufficientPermissionsError": "Only admin can delete users"}
    headers = {'Authorization': f'Bearer {token_user}'}
    response = await test_app.delete("/users/2", headers=headers)
    assert response.status_code == 403
    assert response.json() == result


async def test_delete_user(test_app):
    result = {"message": "User deleted successfully"}
    headers = {'Authorization': f'Bearer {token_admin}'}
    response = await test_app.delete("/users/2", headers=headers)
    assert response.status_code == 200
    assert response.json() == result


async def test_delete_user_invalid_data(test_app):
    result = {"NotFoundError": "User not found"}
    headers = {'Authorization': f'Bearer {token_admin}'}
    response = await test_app.delete("/users/3", headers=headers)
    assert response.status_code == 404
    assert response.json() == result
