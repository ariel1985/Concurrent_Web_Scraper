import pytest
from httpx import AsyncClient
from app.api import app

@pytest.mark.asyncio
async def test_read_data():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/data")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_create_link():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/links", json={"link": "https://example.com"})
    assert response.status_code == 200
    assert response.json()["link"] == "https://example.com"

@pytest.mark.asyncio
async def test_delete_link():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # First create a link to delete
        create_response = await ac.post("/links", json={"link": "https://example.com"})
        link_id = create_response.json()["id"]

        # Then delete the created link
        delete_response = await ac.delete(f"/links/{link_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Link deleted successfully"
