import pytest
from httpx import AsyncClient
from app.main import app
import warnings
warnings.filterwarnings("ignore", category=PendingDeprecationWarning)

@pytest.mark.asyncio
async def test1():
  async with AsyncClient(app=app, base_url="http://test") as client:
    # crea
    resp = await client.post("/books/", \
                             json={"title": "book1", "author": "Name Surname"})
    assert resp.status_code == 201
    book = resp.json()
    assert book["title"] == "book1"
    assert book["author"] == "Name Surname"