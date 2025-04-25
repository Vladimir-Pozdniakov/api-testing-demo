from requests import Response

from framework.api.api_client import APIClient
from framework.api.endpoints import RandomAPI
from framework.api.models.response_types import PoemResponse
from settings import API_URL


class RandomService:
    """Service for interacting with Random API endpoints"""

    def __init__(self, api_client: APIClient = None):
        self.api_client = api_client or APIClient(base_url=API_URL)

    def get_random_poem(self) -> tuple[list[PoemResponse], Response]:
        """
        Get random poem

        Returns:
            Random data
        """
        response = self.api_client.get(RandomAPI.base)
        poems = [PoemResponse.model_validate(item) for item in response.json()]
        return poems, response
