from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_list_passengers_should_return_204_when_no_passenger():
    response = client.get("/passengers")
    assert response.status_code == 204


def test_list_passengers_should_return_200_with_passengers():
    response = client.get("/passengers")
    assert response.status_code == 200
