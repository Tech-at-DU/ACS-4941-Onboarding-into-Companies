from datetime import date

import pytest

import dates
from app import create_app


@pytest.fixture
def client():
    return create_app().test_client()


def test_create_todo(client):
    response = client.post("/todos", json={"title": "Write README"})
    assert response.status_code == 201
    body = response.get_json()
    assert body["title"] == "Write README"
    assert body["done"] is False


def test_create_todo_requires_title(client):
    response = client.post("/todos", json={"title": "   "})
    assert response.status_code == 400


def test_get_missing_todo_returns_404(client):
    assert client.get("/todos/999").status_code == 404


def test_mark_todo_done(client):
    todo_id = client.post("/todos", json={"title": "Ship it"}).get_json()["id"]
    response = client.patch(f"/todos/{todo_id}", json={"done": True})
    assert response.get_json()["done"] is True


def test_filter_by_done(client):
    first = client.post("/todos", json={"title": "A"}).get_json()["id"]
    client.post("/todos", json={"title": "B"})
    client.patch(f"/todos/{first}", json={"done": True})

    open_todos = client.get("/todos?done=false").get_json()
    assert [t["title"] for t in open_todos] == ["B"]


def test_delete_todo(client):
    todo_id = client.post("/todos", json={"title": "Temp"}).get_json()["id"]
    assert client.delete(f"/todos/{todo_id}").status_code == 204
    assert client.get(f"/todos/{todo_id}").status_code == 404


def test_filter_by_created_after(client, monkeypatch):
    monkeypatch.setattr(dates, "today", lambda: date(2025, 12, 31))
    client.post("/todos", json={"title": "Old"})
    monkeypatch.setattr(dates, "today", lambda: date(2026, 2, 2))
    client.post("/todos", json={"title": "New"})

    recent = client.get("/todos?created_after=2026-01-01").get_json()
    assert [t["title"] for t in recent] == ["New"]


def test_parse_date():
    assert dates.parse_date("2026-01-01") == date(2026, 1, 1)
