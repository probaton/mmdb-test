from requests import get as get_request, post as post_request
from Response import Response

def get(id=""):
    response = get_request("http://localhost:5000/movies/" + id)
    return Response(response.status_code, response.json())

def post(data={}):
    response = post_request("http://localhost:5000/movies/", data=data)
    return Response(response.status_code, response.json())
    