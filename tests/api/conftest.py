import pytest
import requests

@pytest.fixture(scope="session")
def api():
    session = requests.Session()
    session.base_url = "https://dummyjson.com"
    return session