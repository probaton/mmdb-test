import pytest
import shutil
import os
import sys

sys.path.append(os.getcwd() + "/api/")
from Store import Store

@pytest.fixture(scope="function", autouse=True)
def reset_db():
    db_dir = "api/db/"
    db_name = "Movies.json"
    try:
        shutil.copyfile("test/reset/db.json", f"{db_dir}{db_name}")
    except (FileNotFoundError):
        os.mkdir(db_dir)
        shutil.copyfile("test/reset/db.json", f"{db_dir}{db_name}")

@pytest.fixture(scope="function")
def movie_db():
    return Store("Movies")