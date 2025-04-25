from typing import Any, Literal

import requests
from requests import Response

from framework.logger import APILogger

# Define HTTP methods type
HTTPMethod = Literal["GET", "POST", "PUT", "PATCH", "DELETE", "HEAD"]


class APIClient:
    """Base class for API clients"""

    def __init__(self, base_url: str = "", headers: dict = None):
        """
        Initialize the API client with base URL and default headers

        Args:
            base_url: Base URL for API endpoints
            headers: Default headers to include in all requests
        """
        self.base_url = base_url
        self.headers = headers or {}
        self.session = requests.Session()

        # Set default headers for the session
        if self.headers:
            self.session.headers.update(self.headers)

    def get(
        self, endpoint: str, params: dict = None, headers: dict = None, **kwargs
    ) -> Response:
        """
        Send GET request

        Args:
            endpoint: API endpoint (will be appended to base_url)
            params: Query parameters
            headers: Additional headers for this request
            **kwargs: Additional arguments to pass to requests.request

        Returns:
            Response object
        """
        return self._request(
            "GET", endpoint, params=params, headers=headers, **kwargs
        )

    def post(
        self,
        endpoint: str,
        data: Any = None,
        json_data: Any = None,
        headers: dict = None,
        **kwargs,
    ) -> Response:
        """
        Send POST request

        Args:
            endpoint: API endpoint (will be appended to base_url)
            data: Form data or request body
            json_data: JSON data (will be serialized)
            headers: Additional headers for this request
            **kwargs: Additional arguments to pass to requests.request

        Returns:
            Response object
        """
        return self._request(
            "POST",
            endpoint,
            data=data,
            json=json_data,
            headers=headers,
            **kwargs,
        )

    def put(
        self,
        endpoint: str,
        data: Any = None,
        json_data: Any = None,
        headers: dict = None,
        **kwargs,
    ) -> Response:
        """
        Send PUT request

        Args:
            endpoint: API endpoint (will be appended to base_url)
            data: Form data or request body
            json_data: JSON data (will be serialized)
            headers: Additional headers for this request
            **kwargs: Additional arguments to pass to requests.request

        Returns:
            Response object
        """
        return self._request(
            "PUT",
            endpoint,
            data=data,
            json=json_data,
            headers=headers,
            **kwargs,
        )

    def patch(
        self,
        endpoint: str,
        data: Any = None,
        json_data: Any = None,
        headers: dict = None,
        **kwargs,
    ) -> Response:
        """
        Send PATCH request

        Args:
            endpoint: API endpoint (will be appended to base_url)
            data: Form data or request body
            json_data: JSON data (will be serialized)
            headers: Additional headers for this request
            **kwargs: Additional arguments to pass to requests.request

        Returns:
            Response object
        """
        return self._request(
            "PATCH",
            endpoint,
            data=data,
            json=json_data,
            headers=headers,
            **kwargs,
        )

    def delete(self, endpoint: str, headers: dict = None, **kwargs) -> Response:
        """
        Send DELETE request

        Args:
            endpoint: API endpoint (will be appended to base_url)
            headers: Additional headers for this request
            **kwargs: Additional arguments to pass to requests.request

        Returns:
            Response object
        """
        return self._request("DELETE", endpoint, headers=headers, **kwargs)

    def _request(
        self, method: HTTPMethod, endpoint: str, headers: dict = None, **kwargs
    ) -> Response:
        """
        Send HTTP request

        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint (will be appended to base_url)
            headers: Additional headers for this request
            **kwargs: Additional arguments to pass to requests.request

        Returns:
            Response object
        """
        # Construct full URL
        url = f"{self.base_url}{endpoint}" if self.base_url else endpoint

        # Merge headers
        request_headers = self.headers.copy()
        if headers:
            request_headers.update(headers)

        # Send request
        response = self.session.request(
            method=method, url=url, headers=request_headers, **kwargs
        )

        # Log request and response
        APILogger.log_api_call(response)

        return response

    def get_json(self, endpoint: str, **kwargs) -> dict | list:
        """
        Send GET request and return JSON response

        Args:
            endpoint: API endpoint
            **kwargs: Additional arguments to pass to get method

        Returns:
            JSON response as dictionary
        """
        response = self.get(endpoint, **kwargs)
        response.raise_for_status()
        return response.json()

    def post_json(self, endpoint: str, json_data: Any, **kwargs) -> dict:
        """
        Send POST request with JSON data and return JSON response

        Args:
            endpoint: API endpoint
            json_data: JSON data to send
            **kwargs: Additional arguments to pass to the Post method

        Returns:
            JSON response as dictionary
        """
        response = self.post(endpoint, json_data=json_data, **kwargs)
        response.raise_for_status()
        return response.json()
