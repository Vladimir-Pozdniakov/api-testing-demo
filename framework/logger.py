import logging
import os
import traceback
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from requests import PreparedRequest, Response

from settings import CONSOLE_LOGS, LOG_DIRECTORY


@dataclass
class ResponseLogData:
    """Class for formatting response log data"""

    timestamp: datetime
    status_code: int
    response_text: str
    headers: dict

    LOG_SEPARATOR = "\n-----\n"

    def format_log_entry(self) -> str:
        """Format response data for logging"""
        return (
            f"Date: {str(self.timestamp.strftime('%Y-%m-%d %H:%M:%S'))}\n"
            f"Response code: {self.status_code}\n"
            f"Response text: {self.response_text}\n"
            f"Response headers: {self.headers}\n"
            f"{self.LOG_SEPARATOR}"
        )


@dataclass
class RequestLogData:
    """Class for formatting request log data"""

    timestamp: datetime
    test_name: Optional[str]
    function_name: str
    method: str
    url: str
    payload: str | bytes | None
    headers: dict

    LOG_SEPARATOR = "\n-----\n"

    def format_log_entry(self) -> str:
        """Format request data for logging"""
        return (
            f"{self.LOG_SEPARATOR}"
            f"Date: {str(self.timestamp.strftime('%Y-%m-%d %H:%M:%S'))}\n"
            f"Test: {self.test_name or 'N/A'}\n"
            f"Function: {self.function_name}\n"
            f"Request method: {self.method}\n"
            f"Request URL: {self.url}\n"
            f"Request headers: {self.headers}\n"
            f"Request data: {self.payload}\n"
        )


class APILogger:
    """Logger for API requests and responses"""

    # Configure Python's logging module
    logger = logging.getLogger("api_test_framework")
    logger.setLevel(logging.INFO)

    # Create a unique log file for this session
    date_now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file_path = os.path.join(LOG_DIRECTORY, f"api_test_log_{date_now}.log")

    # File handler
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(logging.INFO)
    logger.addHandler(file_handler)

    # Console handler (optional)
    if CONSOLE_LOGS:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        logger.addHandler(console_handler)

    @classmethod
    def log_api_call(cls, response: Response) -> None:
        """Log both request and response for an API call"""
        cls.log_request(response.request)
        cls.log_response(response)

    @classmethod
    def log_request(cls, request: PreparedRequest) -> None:
        """Log HTTP request details"""
        # Get a test name from pytest if available
        test_name = os.environ.get("PYTEST_CURRENT_TEST")

        # Get calling function name
        stack = traceback.extract_stack()
        function_name = stack[-3][2]

        log_data = RequestLogData(
            timestamp=datetime.now(),
            test_name=test_name,
            function_name=function_name,
            method=request.method,
            url=request.url,
            headers=dict(request.headers),
            payload=request.body,
        )

        cls.logger.info(log_data.format_log_entry())

    @classmethod
    def log_response(cls, response: Response) -> None:
        """Log HTTP response details"""
        log_data = ResponseLogData(
            timestamp=datetime.now(),
            status_code=response.status_code,
            response_text=response.text,
            headers=dict(response.headers),
        )

        cls.logger.info(log_data.format_log_entry())

    @classmethod
    def log_info(cls, message: str) -> None:
        """Log a general information message"""
        cls.logger.info(message)

    @classmethod
    def log_error(cls, message: str) -> None:
        """Log error message"""
        cls.logger.error(message)
