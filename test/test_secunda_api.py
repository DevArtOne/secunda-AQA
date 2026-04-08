#-----------------API------------------
# -----------------The men's sport watches------------------
def test_api_men_sport_watches_request_grid(home_page, page):
    with page.expect_request("**/api/catalog/grid") as request_info:
        home_page.get_mens_sport_watches()

    request = request_info.value
    assert request.method == "POST"

def test_api_men_sport_watches_response_grid(home_page, page):
    with page.expect_response("**/api/catalog/grid") as response_info:
        home_page.get_mens_sport_watches()

    response = response_info.value
    assert response.status == 200
    data = response.json()
    assert "items" in data
    assert len(data["items"]) > 0
    assert isinstance(data["items"], list) #Це перевірка типу. Вона гарантує, що data["items"] є саме списком.
    # assert any("id" in item for item in data["items"]) #Перевірка, що хоча б один елемент має id
    assert all("id" in item for item in data["items"]) #Перевірка, що всі елементи мають id

def test_api_men_sport_watches_request_filter(home_page, page):
    with page.expect_request("**/api/catalog/filter") as request_info:
        home_page.get_mens_sport_watches()

    request = request_info.value
    assert request.method == "POST"

def test_api_men_sport_watches_response_filter(home_page, page):
    with page.expect_response("**/api/catalog/filter") as response_info:
        home_page.get_mens_sport_watches()

    # response = response_info.value
    # assert response.status == 200
    # data = response.json()
    # assert "blocks" in data
    # assert isinstance(data["blocks"], dict)
    # assert len(data["blocks"]) > 0
    # # Перевіряємо, що хоча б один блок має словник значень з id
    # assert any(
    #     isinstance(block, dict)
    #     and isinstance(block.get("values"), dict)
    #     and block["values"]
    #     and all("id" in item for item in block["values"].values())
    #     for block in data["blocks"].values()
    # )

    response = response_info.value
    assert response.status == 200
    data = response.json()
    assert "blocks" in data
    assert "indexing" in data["blocks"]
    assert isinstance(data["blocks"], dict)
    indexing = data["blocks"]["indexing"]
    assert isinstance(indexing, dict)
    assert "name" in indexing and isinstance(indexing["name"], str)
    assert "type" in indexing and indexing["type"] in {"multiselect", "select"}
    assert "values" in indexing and isinstance(indexing["values"], dict)
    assert len(indexing["values"]) > 0
    # Перевірка, що кожне значення має id і name
    assert all(
        isinstance(item, dict)
        and "id" in item
        and "name" in item
        and "sid" in item
        for item in indexing["values"].values()
    )

#-----------------The men's sport watches------------------


#-----------------The women's sport watches------------------
def test_api_women_classic_watches_request(home_page, page):
    with page.expect_request("**/api/catalog/grid") as request_info:
        home_page.get_women_classic_watches()

    request = request_info.value
    assert request.method == "POST"

def test_api_women_classic_watches_response(home_page, page):
    with page.expect_response("**/api/catalog/grid") as response_info:
        home_page.get_women_classic_watches()

    response = response_info.value
    assert response.status == 200
    data = response.json()
    assert "items" in data
    assert len(data["items"]) > 0
    assert isinstance(data["items"], list)
    assert all("id" in item for item in data["items"])
#-----------------The women's sport watches------------------
#-----------------API------------------
