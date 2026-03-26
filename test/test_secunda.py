import re

import pytest
from pages.secunda_pages import SecundaPage
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError, expect

# --------------------------------
r""" helper‑функція, щоб стабільно перевіряти переходи, коли лінк може:
1.Відкритися в новій вкладці (popup)
2.Відкритися в цій же вкладці"""

def click_link_and_expect_url(page, click_fn, expected_url, popup_timeout_ms=2000, wait_state=None):
    try:
        with page.context.expect_page(timeout=popup_timeout_ms) as popup_info:
            click_fn()
        popup_page = popup_info.value
        if wait_state:
            popup_page.wait_for_load_state(wait_state)
        expect(popup_page).to_have_url(expected_url)
    except PlaywrightTimeoutError:
        if wait_state:
            page.wait_for_load_state(wait_state)
        expect(page).to_have_url(expected_url)
#--------------------------------

@pytest.fixture
def home_page(page):
    obj = SecundaPage(page)
    obj.open()
    return obj


# -----------------Burger menu-------------------------------
def test_burger_menu(home_page, page):
    page.set_viewport_size({"width": 375, "height": 812})
    # home_page.get_menu()
    home_page.get_burger_menu()
    home_page.get_burger_menu_items()

    expect(home_page.get_burger_menu()).to_be_visible()
    expect(home_page.get_burger_menu_items()).to_be_hidden()

    home_page.click_burger_menu()
    expect(home_page.get_burger_menu_items()).to_be_visible()
# -----------------Burger menu-------------------------------

# -----------------The men's sport watches------------------
def test_men_sport_watches(home_page, page):
    home_page.get_mens_sport_watches()
    expect(page).to_have_url(re.compile(r"/versiya:sport_stat:cholovichi/"))
# -----------------The men's sport watches------------------
