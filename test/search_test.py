from search_requests import get

def test_get_with_single_title_match():
    response = get("Star Shreks")

    assert response.status_code == 200
    assert response.data == [{
        "name": "Star Shreks",
        "release_date": "2001",
        "id": "1a13569f-bb3c-4c64-9126-680b3bce24de"
    }]

def test_get_with_multiple_title_matches():
    response = get("Star")

    assert response.status_code == 200
    assert response.data == [{
        "name": "Star Shreks",
        "release_date": "2001",
        "id": "1a13569f-bb3c-4c64-9126-680b3bce24de"
    },
    {
        "name": "Star Shmores",
        "release_date": "1977",
        "id": "6f439813-5ecb-46e0-a88b-4809f43b331e"
    }]

def test_get_with_title_and_date_matches():
    response = get("2001")

    assert response.status_code == 200
    assert response.data == [{
        "name": "Star Shreks",
        "release_date": "2001",
        "id": "1a13569f-bb3c-4c64-9126-680b3bce24de"
    },
    {
        "name": "2001: A Shpace Shmodyssey",
        "release_date": "1968",
        "id": "0de7ddaa-6858-4d3c-b992-c9cb686849ef"
    }]

def test_get_with_no_matches():
    search_term = "Not Actually a Movie"
    response = get(search_term)

    assert response.status_code == 200
    assert response.data == f"Your search for <{search_term}> did not yield any results"

def test_get_without_search_term():
    response = get()

    assert response.status_code == 400
    assert response.data == "The <search_term> field is required"
