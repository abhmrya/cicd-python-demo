from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}


def test_index_reports_environment(monkeypatch):
    monkeypatch.setenv("APP_ENV", "staging")
    monkeypatch.setenv("APP_VERSION", "abc123")
    body = client.get("/").json()
    assert body["environment"] == "staging"
    assert body["version"] == "abc123"


def test_add():
    assert client.get("/add?a=2&b=3").json() == {"result": 5}


def test_add_rejects_bad_input():
    assert client.get("/add?a=x&b=3").status_code == 422