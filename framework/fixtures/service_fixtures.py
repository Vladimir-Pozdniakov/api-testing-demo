import pytest

from framework.api.services.author_service import AuthorService
from framework.api.services.lines_services import LinesService
from framework.api.services.random_services import RandomService
from framework.api.services.title_service import TitleService


@pytest.fixture
def author_service(api_client):
    return AuthorService(api_client)


@pytest.fixture
def title_service(api_client):
    return TitleService(api_client)


@pytest.fixture
def random_service(api_client):
    return RandomService(api_client)


@pytest.fixture
def lines_service(api_client):
    return LinesService(api_client)
