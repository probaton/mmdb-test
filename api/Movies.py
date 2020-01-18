from flask_restful import Resource
from flask import request
from Store import Store

class Movies(Resource):
    def __init__(self):
        self.__db = Store("Movies")

    def get(self, id=None):
        if id:
            try:
                return self.__db.get_by_id(id)[0], 200
            except (IndexError):
                return "Movie not found", 404
        else: 
            return self.__db.get_all()

    def post(self):
        new_movie = {}
        try:
            new_movie["name"] = request.values["name"]
            new_movie["release_date"] = request.values["release_date"]
        except:
            return "The <name> and <release_date> fields are required", 400
        
        duplicate = self.__db.find(new_movie["name"], new_movie["release_date"])
        if duplicate:
            return "There is already an entry with that <name> and <release_date>", 400

        return self.__db.insert(new_movie), 201
