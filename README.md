# REST API Testing Framework

A test automation framework for REST API testing using Python,
pytest, and requests.

## Project Overview

This framework provides a structured approach to API testing with features like:

- Object-oriented design with service-based architecture
- Detailed request and response logging
- HTML test reporting
- Environment configuration management
- Response time validation
- Pydantic models for response validation

## Requirements

- Python 3.11
- UV package manager
- Docker + docker-compose

## Project Structure

```
api-testing-demo/
├── framework/                      # Core framework components
│   ├── api/                        # API interaction layer
│   │   ├── api_client.py           # Base HTTP client
│   │   ├── endpoints.py            # API endpoint definitions
│   │   ├── models/                 # Response models
│   │   │   └── response_types.py   # Pydantic models
│   │   └── services/               # Service layer for API operations
│   │       ├── author_service.py
│   │       ├── lines_services.py
│   │       ├── random_services.py
│   │       └── title_service.py
│   ├── fixtures/                   # pytest fixtures
│   │   └── service_fixtures.py
│   └── logger.py                   # Logging functionality
├── reports/                        # Test reports and logs
│   ├── logs/                       # API request/response logs
│   └── report.html                 # HTML test report
├── tests/                          # Test cases
│   ├── author_api_test.py          # Author API tests
│   ├── data/                       # Test data
│   │   └── test_data.py
│   └── title_api_test.py           # Title API tests
├── utilities/                      # Utility functions
│   └── date_time_helper.py         # Date/time utilities
├── conftest.py                     # pytest configuration
├── pyproject.toml                  # Project dependencies
├── pytest.ini                      # pytest settings
├── settings.py                     # Framework settings
└── .env                            # Environment variables
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Vladimir-Pozdniakov/api-testing-demo.git
   cd api-testing-demo
   ```

2. Create and activate a virtual environment:
   ```bash
   uv venv --python 3.11
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   uv pip install -r pyproject.toml
   ```

## Configuration

The framework uses environment variables for configuration,
which can be set in the `.env` file.
   ```bash
   cp .env.example .env
   ```

Key configuration options:
- `API_URL`: Base URL for the API under test
- `LOCAL_RUNNER`: Set to 1 for local execution, 0 for CI environment
- `CONSOLE_LOGS`: Set to 1 to enable console logging, 0 to disable

## Set up the REST API application for testing (SUT)

1. Clone the repository:
   ```bash
   git clone https://github.com/thundercomb/poetrydb.git
   cd poetrydb
   ```

2. Run the SUT app in docker containers:
   ```bash
   docker-compose up -d
   ```
3. The SUT app will be available by url: `http://localhost:3000`

**NOTE**

If you are having trouble running the SUT application locally in Docker
containers, change the following files to the following content:

`Dockerfile` :

```dockerfile
FROM --platform=linux/amd64 ruby:2.6-bullseye

RUN apt-get update && apt-get install -y wget gnupg

RUN wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | \
    gpg --dearmor | \
    tee /usr/share/keyrings/mongodb.gpg > /dev/null

RUN echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb.gpg ] https://repo.mongodb.org/apt/debian bullseye/mongodb-org/6.0 main" | \
    tee /etc/apt/sources.list.d/mongodb-org-6.0.list

RUN apt-get update && apt-get install -y mongodb-org-tools

RUN mkdir /poetrydb
COPY ./ /poetrydb
WORKDIR /poetrydb/app
RUN bundle install
```

`app/Gemfile` :
```
source "https://rubygems.org"
ruby '2.6.10'
gem 'sinatra', '2.0.5'
gem 'unicorn'
gem 'mongo', '2.13.0'
gem 'json'
```

## Running Tests

### Run all tests:
```bash
pytest -s
```

### Run a specific test file:
```bash
pytest tests/author_api_test.py
```

### Run tests by marker:
```bash
pytest -m smoke
```

### Run tests with a specific name pattern:
```bash
pytest -k test_get_all_authors
```

### View test report:
After running tests, open the HTML report at `reports/report.html`

## Test Cases

| ID | Test Name | Description | API Endpoint | Assertions | Markers |
|----|-----------|-------------|--------------|------------|---------|
| 1 | test_get_all_authors | Verify retrieving all authors | GET /author | - Status code is 200<br>- Response contains expected authors<br>- Response time < 0.5s | api, smoke |
| 2 | test_get_all_author_poems | Verify retrieving poems by author | GET /author/{name} | - Status code is 200<br>- Response contains expected poems<br>- Response time < 0.5s | api, smoke |
| 3 | test_get_all_titles | Verify retrieving all titles | GET /title | - Status code is 200<br>- Response contains expected titles<br>- Response time < 0.5s | api, smoke |
| 4 | test_get_poem_by_full_title_match | Verify retrieving poem by exact title | GET /title/{name} | - Status code is 200<br>- Response contains exactly one poem<br>- Response contains expected poem<br>- Response time < 0.5s | api, smoke |

**Explanation:

These tests covered both functional and non-functional aspects of the API.

The purpose of such tests are:
* Status and performance validations for availability and speed.
* Content validations to check functional correctness.
* Markers for organizing and prioritizing test execution.

This combination ensures the APIs are:
* Available
* Performant
* Returning correct data
* Easy to manage in test execution workflows

## Framework Features

### 1. API Client
- Session-based HTTP client
- Support for all HTTP methods (GET, POST, PUT, PATCH, DELETE)
- Automatic URL construction
- Default and custom headers support
- JSON handling utilities

### 2. Service Layer
- Object-oriented approach with service classes for each API domain
- Clean separation of concerns
- Reusable API operations

### 3. Logging
- Detailed request and response logging
- Timestamp information
- Test context in logs
- Configurable log locations

### 4. Response Validation
- Pydantic models for response validation
- Type checking and data validation
- Response time assertions

### 5. Test Organization
- Markers for test categorization (api, smoke, regression)
- Fixtures for test setup and teardown
- Parameterized tests for data-driven testing

### 6. Reporting
- HTML test reports
- Environment information in reports
- Test execution details
- Pass/fail statistics
