import os
from tinydb import TinyDB, where, Query
from uuid import uuid4

class Store():
    __db_dir = "api/db/"

    def __init__(self, db_name):
        self.__db_path = f"{self.__db_dir}{db_name}.json"

    def __get_db(self):
        try:
            return TinyDB(self.__db_path)
        except (FileNotFoundError):
            os.mkdir(self.__db_dir)
            os.mknod(self.__db_path)
            return TinyDB(self.__db_path)

    def insert(self, new_object):
        new_object["id"] = str(uuid4())
        self.__get_db().insert(new_object)
        return new_object["id"]
 
    def get_by_id(self, id):
        query = Query().id == id
        try:
            return self.__get_db().search(query)[0]
        except (IndexError):
            return None

    def get_all(self):
        return self.__get_db().all()

    def find(self, title, release_date):
        query = Query()
        return self.__get_db().search((query.title == title) & (query.release_date == release_date)) 

    def search(self, search_term):
        query = Query()
        return self.__get_db().search((query.title.search(search_term + "+")) | (query.release_date.search(search_term + "+")))
