from fastapi.testclient import TestClient
from api import app
client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_text_analysis():
    response = client.post("/analyze/text", json={"resume_text": "Python FastAPI PostgreSQL SQL Git REST API machine learning and RAG"})
    assert response.status_code == 200
    assert "python" in response.json()["skills"]
