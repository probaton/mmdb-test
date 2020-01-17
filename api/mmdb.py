from flask import Flask
from flask_restful import Resource, Api

from Movies import Movies

app = Flask("The Mock Movie Database")
api = Api(app)

api.add_resource(Movies, "/movies/<string:id>", "/movies", "/movies/")

if __name__ == "__main__":
    app.run(debug=True)
