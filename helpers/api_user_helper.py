import requests
import uuid

BASE_URL = "https://stellarburgers.education-services.ru/api"

class ApiUserHelper:
    def create_user():
        payload = {
            "email": f"test_{uuid.uuid4()}@mail.ru",
            "password": "123456",
            "name": "Test User"
        }

        response = requests.post(f"{BASE_URL}/auth/register", json=payload)
        access_token = response.json()["accessToken"]

        return payload, access_token


    def delete_user(token):
        headers = {"Authorization": token}
        requests.delete(f"{BASE_URL}/auth/user", headers=headers)