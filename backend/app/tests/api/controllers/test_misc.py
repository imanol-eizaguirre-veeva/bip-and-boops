from fastapi.testclient import TestClient

from ....main import app
from ....core.config import settings

client = TestClient(app)


def test_read_main():
    response = client.get(f"{settings.API_V1_STR}")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
