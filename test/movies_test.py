from util import is_valid_uuid
from movie_requests import get, post


def test_get_with_valid_id():
    response = get("1a13569f-bb3c-4c64-9126-680b3bce24de")

    assert response.status_code == 200
    assert response.data == {
        "title": "Star Shreks",
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
            "title": "Star Shreks",
            "release_date": "2001"
        },
        {
            "title": "2001: A Shpace Shmodyssey",
            "release_date": "1968",
            "id": "0de7ddaa-6858-4d3c-b992-c9cb686849ef"
        },
        {
            "id": "6f439813-5ecb-46e0-a88b-4809f43b331e",
            "title": "Star Shmores",
            "release_date": "1977"
        }
    ]

def test_post_with_valid_data(movie_db):
    movie_title = "The Schmatrix"
    release_date = "1999"
    response = post({
        "title": movie_title,
        "release_date": release_date
    })

    assert response.status_code == 201
    assert is_valid_uuid(response.data)
    assert movie_db.get_by_id(response.data) == {
        "id": response.data,
        "title": movie_title,
        "release_date": release_date
    }

def test_post_without_title(movie_db):
    response = post({ "release_date": "1970" })

    assert response.status_code == 400
    assert response.data == "The <title> and <release_date> fields are required"
    assert len(movie_db.get_all()) == 3

def test_post_without_release_date(movie_db):
    response = post({ "title": "Schmurassic Schmark" })

    assert response.status_code == 400
    assert response.data == "The <title> and <release_date> fields are required"
    assert len(movie_db.get_all()) == 3

def test_post_without_data(movie_db):
    response = post()

    assert response.status_code == 400
    assert response.data == "The <title> and <release_date> fields are required"
    assert len(movie_db.get_all()) == 3

def test_post_with_extra_field(movie_db):
    movie_title = "Return of the Killer Schmomatoes"
    release_date = "1989"
    response = post({
        "title": movie_title,
        "release_date": release_date,
        "i_dont_belong_here": "What the hell am I doing here"
    })

    assert response.status_code == 201
    assert is_valid_uuid(response.data)
    assert movie_db.get_by_id(response.data) == {
        "id": response.data,
        "title": movie_title,
        "release_date": release_date
    }
