from requests import Response

from framework.api.api_client import APIClient
from framework.api.endpoints import LinesAPI
from framework.api.models.response_types import PoemResponse
from settings import API_URL


class LinesService:
    """Service for interacting with Lines API endpoints"""

    def __init__(self, api_client: APIClient = None):
        self.api_client = api_client or APIClient(base_url=API_URL)

    def get_poem_by_text_in_lines(
        self, text: str
    ) -> tuple[list[PoemResponse], Response]:
        """
        Get lines by number

        Args:
            text: Text presented in lines

        Returns:
            List of lines
        """
        response = self.api_client.get(LinesAPI.by_line_text(text))
        poems = [PoemResponse.model_validate(item) for item in response.json()]
        return poems, response
