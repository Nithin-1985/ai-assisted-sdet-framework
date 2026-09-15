import requests
from config.logger import setup_logger
logger = setup_logger(__name__)


class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")

    def get_user(self, user_id):
        logger.info(f"Sending GET request for user ID: {user_id}")
        return requests.get(
            f"{self.base_url}/users/{user_id}"
        )

    def create_user(self, payload):
        logger.info(f"Sending POST request to create user")
        return requests.post(
            f"{self.base_url}/users",
            json=payload
        )

    def update_user(self, user_id, payload):
        logger.info(f"Sending PUT request to update user ID: {user_id}")
        return requests.put(
            f"{self.base_url}/users/{user_id}",
            json=payload
        )

    def delete_user(self, user_id):
        logger.info(f"Sending DELETE request for user ID: {user_id}")
        return requests.delete(
            f"{self.base_url}/users/{user_id}"
        )