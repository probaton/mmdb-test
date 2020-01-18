from requests import get as get_request
from Response import Response

def get(search_term=""):
    response = get_request("http://localhost:5000/search/" + search_term)
    return Response(response.status_code, response.json())
