import logging

import pytest

from fixtures.app import App

logger = logging.getLogger("api")



def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        help="enter api url",
        default="https://stores-tests-api.herokuapp.com",
    )


@pytest.fixture
def app(request):
    url = request.config.getoption('--api-url')
    logger.info(f"Start api tests, url is {url}")
    return App(url)
