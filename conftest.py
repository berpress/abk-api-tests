import pytest

from fixtures.app import App


def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        help="enter api url",
        default="https://stores-tests-api.herokuapp.com/",
    )


@pytest.fixture
def app(request):
    url = request.config.getoption('--api-url')
    return App(url)
