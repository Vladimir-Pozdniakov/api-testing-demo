from requests import Response

from framework.api.api_client import APIClient
from framework.api.endpoints import AuthorAPI
from framework.api.models.response_types import AuthorsResponse, PoemResponse
from settings import API_URL


class AuthorService:
    """Service for interacting with Author API endpoints"""

    def __init__(self, api_client: APIClient = None):
        self.api_client = api_client or APIClient(base_url=API_URL)

    def get_all_authors(self) -> tuple[AuthorsResponse, Response]:
        """
        Get all authors

        Returns:
            List of authors
        """
        response = self.api_client.get(AuthorAPI.base)
        authors = AuthorsResponse.model_validate(response.json())
        return authors, response

    def get_poems_by_author(
        self, author: str
    ) -> tuple[list[PoemResponse], Response]:
        """
        Get all author's poems

        Args:
            author: Author name

        Returns:
            Poems data
        """
        response = self.api_client.get(AuthorAPI.by_name(author))
        poems = [PoemResponse.model_validate(item) for item in response.json()]
        return poems, response
