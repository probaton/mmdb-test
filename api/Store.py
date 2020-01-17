import os
from tinydb import TinyDB, where, Query
from uuid import uuid4

class Store():
    db_path = ""

    def __init__(self, db_name):
        self.db_path = f"api/db/{db_name}.json"

    def get_db(self):
        try:
            return TinyDB(self.db_path)
        except (FileNotFoundError):
            os.mknod(self.db_path)
            return TinyDB(self.db_path)

    def insert(self, new_object):
        new_object["id"] = str(uuid4())
        self.get_db().insert(new_object)
 
    def get(self, id):
        query = Query().id == id
        return self.get_db().search(query)

    def search(self, attribute, search_term):
        query = Query()[attribute].search(search_term + "+")
        return self.get_db().search(query)
