from flask_restful import Api, Resource
from Store import Store

class Movies(Resource):
    db = None

    def __init__(self):
        self.db = Store("Movies")

    def get(self, id=None):
        if id:
            return self.db.get(id)[0]
        else: 
            return self.db.get_all()

    def post(self, name):
        return self.db.insert({ "name": name })
