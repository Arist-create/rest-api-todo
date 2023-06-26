import pytest
from httpx import AsyncClient
from main import app
from tests import *
import pytest_asyncio
import asyncio


@pytest_asyncio.fixture
async def test_app():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
