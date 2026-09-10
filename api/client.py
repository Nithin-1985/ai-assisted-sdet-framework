import requests


class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")

    def get_user(self, user_id):
        return requests.get(
            f"{self.base_url}/users/{user_id}"
        )

    def create_user(self, payload):
        return requests.post(
            f"{self.base_url}/users",
            json=payload
        )

    def update_user(self, user_id, payload):
        return requests.put(
            f"{self.base_url}/users/{user_id}",
            json=payload
        )

    def delete_user(self, user_id):
        return requests.delete(
            f"{self.base_url}/users/{user_id}"
        )