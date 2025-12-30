from config.urls import Urls
import requests
import uuid

class ApiUserHelper:

    @staticmethod
    def create_user():
        payload = {
            "email": f"test_{uuid.uuid4()}@mail.ru",
            "password": "123456",
            "name": "Test User"
        }

        response = requests.post(
            f"{Urls.BASE_URL}{Urls.API_PREFIX}{Urls.AUTH_REGISTER}",
            json=payload
        )

        access_token = response.json()["accessToken"]
        return payload, access_token

    @staticmethod
    def delete_user(token):
        headers = {"Authorization": token}

        response = requests.delete(
            f"{Urls.BASE_URL}{Urls.API_PREFIX}{Urls.AUTH_USER}",
            headers=headers
        )
        return response.status_code

