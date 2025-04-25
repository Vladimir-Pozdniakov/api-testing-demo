from requests import Response

from framework.api.api_client import APIClient
from framework.api.endpoints import TitleAPI
from framework.api.models.response_types import PoemResponse, TitlesResponse
from settings import API_URL


class TitleService:
    """Service for interacting with Title API endpoints"""

    def __init__(self, api_client: APIClient = None):
        self.api_client = api_client or APIClient(base_url=API_URL)

    def get_all_titles(self) -> tuple[TitlesResponse, Response]:
        """
        Get all titles

        Returns:
            List of title data
        """
        response = self.api_client.get(TitleAPI.base)
        titles = TitlesResponse.model_validate(response.json())
        return titles, response

    def get_poem_by_title(
        self, title: str
    ) -> tuple[list[PoemResponse], Response]:
        """
        Get title by name

        Args:
            title: Title name

        Returns:
            List of poems with this title
        """
        response = self.api_client.get(TitleAPI.by_name(title))
        poems = [PoemResponse.model_validate(item) for item in response.json()]
        return poems, response
