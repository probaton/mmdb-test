from flask_restful import Resource, reqparse
from flask import request
from Store import Store

class Movies(Resource):
    db = None

    def __init__(self):
        self.db = Store("Movies")

    def get(self, id=None):
        if id:
            try:
                return self.db.get(id)[0], 200
            except (IndexError):
                return "Movie not found", 404
        else: 
            return self.db.get_all()

    def post(self):
        new_movie = {}
        try:
            new_movie["name"] = request.values["name"]
            new_movie["release_date"] = request.values["release_date"]
        except:
            return "The <name> and <release_date> fields are required", 400

        return self.db.insert(new_movie), 201
