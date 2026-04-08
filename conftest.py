import pytest
from pages.secunda_pages import SecundaPage


@pytest.fixture
def home_page(page):
    obj = SecundaPage(page)
    obj.open()
    return obj


@pytest.fixture
def secunda_page(page):
    return SecundaPage(page)