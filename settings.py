import os

from dotenv import load_dotenv

load_dotenv()

# System Under Test Environment
LOCAL_RUNNER = bool(int(os.getenv("LOCAL_RUNNER", 0)))
API_URL = os.getenv("API_URL").rstrip("/")

# Logging Configuration
LOG_DIRECTORY = os.path.join(os.path.dirname(__file__), "reports/logs")
os.makedirs(LOG_DIRECTORY, exist_ok=True)
CONSOLE_LOGS = bool(int(os.getenv("CONSOLE_LOGS", 0)))

# Reporting Configuration
REPORT_DIRECTORY = os.path.join(os.path.dirname(__file__), "reports")
os.makedirs(REPORT_DIRECTORY, exist_ok=True)
