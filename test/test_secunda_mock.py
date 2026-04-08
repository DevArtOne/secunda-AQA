import re

from playwright.sync_api import expect

#-----------------Block request-------------------
def test_block_secunda_images(secunda_page, page):
    page.route("**/api/catalog/grid", lambda route: route.abort())
    secunda_page.open()

    with page.expect_event(
        "requestfailed",
        lambda request: "/api/catalog/grid" in request.url,
    ) as failed_request_info:
        secunda_page.get_mens_sport_watches()

    failed_request = failed_request_info.value
    assert failed_request.failure is not None
    assert failed_request.method == "POST"
#-----------------Block request-------------------

#-----------------Mock API-----------------------
def test_mock_watches(secunda_page, page):

    def mock_watches(route):
        route.fulfill(
            status=200,
            content_type="application/json",
            body='{"items":[{"id":1,"name":"Kalugala"}]}'
        )

    page.route("**/api/catalog/grid", mock_watches)

    secunda_page.open()

    with page.expect_response("**/api/catalog/grid") as response_info:
        secunda_page.get_mens_sport_watches()

    assert response_info.value.status == 200
    data = response_info.value.json()
    assert data["items"][0]["name"] == "Kalugala"
    expect(page.get_by_text("Kalugala").first).to_be_visible()


def test_error_loading_users(secunda_page, page):
    page.route("**/api/catalog/grid", lambda route: route.abort())
    secunda_page.open()

    with page.expect_request("**/api/catalog/grid") as request_info:
        secunda_page.get_mens_sport_watches()

    request = request_info.value
    assert request.method == "POST"
    expect(page).to_have_url(re.compile(r"https://secunda\.com\.ua/?#?$"))
#-----------------Mock API-----------------------

# ----------------API------------------
