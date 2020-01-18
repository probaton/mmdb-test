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
        return new_object["id"]
 
    def get_by_id(self, id):
        query = Query().id == id
        return self.get_db().search(query)

    def get_all(self):
        return self.get_db().all()

    def find(self, name, release_date):
        query = Query()
        return self.get_db().search((query.name == name) & (query.release_date == release_date)) 

    def search(self, search_term):
        query = Query()
        return self.get_db().search((query.name.search(search_term + "+")) | (query.release_date.search(search_term + "+")))
