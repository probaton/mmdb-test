from flask_restful import Resource
from Store import Store

class Search(Resource):
    def __init__(self):
        self.db = Store("Movies")

    def get(self, search_term=None):
        if not search_term:
            return "The <search_term> field is required", 400

        result = self.db.search(search_term)
        if not result:
            return f"Your search for <{search_term}> did not yield any results", 200

        return result, 200 
