import pytest
from movie_requests import get, post

def test_get_with_valid_id():
    response = get("1a13569f-bb3c-4c64-9126-680b3bce24de")

    assert response.status_code == 200
    assert response.data == {
            "name": "Star Shreks",
            "release_date": "2001",
            "id": "1a13569f-bb3c-4c64-9126-680b3bce24de"
        }

def test_get_with_invalid_id():
    response = get("not-a-valid-id")

    assert response.status_code == 404
    assert response.data == "Movie not found", "Incorrect error message"

def test_get_without_id():
    response = get()

    assert response.status_code == 200
    assert response.data == [
            {
                "id": "1a13569f-bb3c-4c64-9126-680b3bce24de",
                "name": "Star Shreks",
                "release_date": "2001"
            },
            {
                "name": "2001: A Shpace Shmodyssey",
                "release_date": "1968",
                "id": "0de7ddaa-6858-4d3c-b992-c9cb686849ef"
            },
            {
                "id": "6f439813-5ecb-46e0-a88b-4809f43b331e",
                "name": "Star Shmores",
                "release_date": "1977"
            }
        ]
