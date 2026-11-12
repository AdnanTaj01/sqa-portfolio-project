import pytest
import requests
from jsonschema import validate

BASE_URL = "https://reqres.in/api"


class TestUsersAPI:
    """API test suite for ReqRes."""

    def test_get_users_returns_200(self):
        response = requests.get(f"{BASE_URL}/users?page=2")

        assert response.status_code == 200
        body = response.json()
        assert len(body["data"]) > 0
        assert body["page"] == 2

    def test_get_single_user_schema(self):
        response = requests.get(f"{BASE_URL}/users/2")
        assert response.status_code == 200

        body = response.json()

        # Schema validation – ensures response contract is stable
        schema = {
            "type": "object",
            "properties": {
                "data": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "email": {"type": "string"},
                        "first_name": {"type": "string"},
                        "last_name": {"type": "string"},
                    },
                    "required": ["id", "email", "first_name", "last_name"],
                }
            },
            "required": ["data"],
        }
        validate(instance=body, schema=schema)

    def test_create_user_post(self):
        payload = {"name": "QA Engineer", "job": "Automation Lead"}
        response = requests.post(f"{BASE_URL}/users", json=payload)

        assert response.status_code == 201
        body = response.json()
        assert body["name"] == "QA Engineer"
        assert "id" in body
        assert "createdAt" in body

    def test_non_existent_user_returns_404(self):
        response = requests.get(f"{BASE_URL}/users/999999")
        assert response.status_code == 404

    @pytest.mark.parametrize("user_id", [1, 2, 3, 4])
    def test_multiple_users_exist(self, user_id):
        response = requests.get(f"{BASE_URL}/users/{user_id}")
        assert response.status_code == 200
        assert response.json()["data"]["id"] == user_id