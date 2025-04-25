from datetime import datetime

import pytest
from pytest_metadata.plugin import metadata_key

from framework.api.api_client import APIClient
from framework.logger import APILogger
from settings import API_URL, LOCAL_RUNNER

pytest_plugins = [
    "framework.fixtures.service_fixtures",
]


@pytest.fixture(scope="session")
def api_client():
    """
    Fixture that provides an API client instance

    Returns:
        APIClient: Configured API client
    """
    # Set default headers for all requests
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    # Create and return the API client
    client = APIClient(base_url=API_URL, headers=headers)

    # Log the test session start
    APILogger.log_info(
        f"Test session started at "
        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )

    yield client

    # Log the test session end
    APILogger.log_info(
        f"Test session ended at "
        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )


# HTML report configuration
def pytest_html_report_title(report):
    report.title = "API Test Automation Report"


def pytest_configure(config):
    config.stash[metadata_key]["API URL"] = API_URL
    config.stash[metadata_key]["Test Framework"] = "Pytest + Requests"
    config.stash[metadata_key]["Environment"] = (
        "Local" if LOCAL_RUNNER else "CI"
    )
