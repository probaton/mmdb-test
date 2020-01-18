from flask_restful import Resource
from flask import request
from Store import Store

class Movies(Resource):
    def __init__(self):
        self.__db = Store("Movies")

    def get(self, id=None):
        if not id:
            return self.__db.get_all()
        
        movie = self.__db.get_by_id(id)
        if not movie:
            return "Movie not found", 404

        return movie, 200

    def post(self):
        new_movie = {}
        try:
            new_movie["title"] = request.values["title"]
            new_movie["release_date"] = request.values["release_date"]
        except:
            return "The <title> and <release_date> fields are required", 400
        
        duplicate = self.__db.find(new_movie["title"], new_movie["release_date"])
        if duplicate:
            return "There is already an entry with that <title> and <release_date>", 400

        return self.__db.insert(new_movie), 201
