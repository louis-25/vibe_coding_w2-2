import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    """루트 엔드포인트 테스트"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Chat API Server"}


def test_health_check():
    """헬스체크 엔드포인트 테스트"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_test_endpoint():
    """테스트 엔드포인트 테스트 - PR 테스트용"""
    response = client.get("/test")
    assert response.status_code == 200
    
    data = response.json()
    assert "message" in data
    assert "version" in data
    assert "features" in data
    assert data["version"] == "1.0.0"
    assert len(data["features"]) == 4
    assert "자동 테스트" in data["features"] 