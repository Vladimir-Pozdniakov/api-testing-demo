import pytest

from framework.api.services.author_service import AuthorService
from tests.data.test_data import exp_authors, exp_emily_dickinson_poems


@pytest.mark.api
class TestAuthorAPI:
    @pytest.mark.smoke
    def test_get_all_authors(self, author_service: AuthorService):
        # When: Get all authors
        authors, resp = author_service.get_all_authors()

        # Then: Response should be correct
        assert resp.status_code == 200, "Response should be 200 OK"

        assert (
            authors.authors == exp_authors
        ), "Response should contain correct authors"

        assert (
            resp.elapsed.total_seconds() < 0.5
        ), "Response should be within 1 second"

    @pytest.mark.smoke
    def test_get_all_author_poems(self, author_service: AuthorService):
        # Given: An author name
        author_name = "Emily Dickinson"

        # When: Get author by name
        poems, resp = author_service.get_poems_by_author(author_name)

        # Then: Response should be correct
        assert resp.status_code == 200, "Response should be 200 OK"

        assert (
            resp.json() == exp_emily_dickinson_poems
        ), "Response should contain correct poems"

        assert (
            resp.elapsed.total_seconds() < 0.5
        ), "Response should be within 1 second"
