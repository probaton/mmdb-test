from flask import Flask
from flask_restful import Resource, Api

from Movies import Movies
from Search import Search

app = Flask("The Mock Movie Database")
api = Api(app)

api.add_resource(Movies, "/movies/<string:id>", "/movies", "/movies/")
api.add_resource(Search, "/search/<string:search_term>", "/search", "/search/")

if __name__ == "__main__":
    app.run(debug=True)
