import pytest

from framework.api.services.title_service import TitleService
from tests.data.test_data import exp_the_moon_maiden_song, exp_titles


@pytest.mark.api
class TestTitleAPI:
    @pytest.mark.smoke
    def test_get_all_titles(self, title_service: TitleService):
        # When: Get all titles
        titles, resp = title_service.get_all_titles()

        # Then: Response should be correct
        assert resp.status_code == 200, "Response should be 200 OK"

        assert (
            titles.titles == exp_titles
        ), "Response should contain correct titles"

        assert (
            resp.elapsed.total_seconds() < 0.5
        ), "Response should be within 1 second"

    @pytest.mark.smoke
    @pytest.mark.parametrize(
        "title_name", ["The Moon Maiden's Song", "The Moon Maid"]
    )
    def test_get_poem_by_full_title_match(
        self, title_name: str, title_service: TitleService
    ):
        # Given: The full and partial title name to match

        # When: Get title by name
        poems, resp = title_service.get_poem_by_title(title_name)

        # Then: Response should be correct
        assert resp.status_code == 200, "Response should be 200 OK"

        assert len(poems) == 1, "Response should contain only one poem"

        assert (
            poems[0].model_dump() == exp_the_moon_maiden_song
        ), "Response should contain correct poem"

        assert (
            resp.elapsed.total_seconds() < 0.5
        ), "Response should be within 1 second"
