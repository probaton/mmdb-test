import pytest
import shutil
import os

@pytest.fixture(scope="module", autouse=True)
def reset_db():
    db_dir = "api/db/"
    db_name = "Movies.json"
    try:
        shutil.copyfile("test/reset/db.json", f"{db_dir}{db_name}")
    except (FileNotFoundError):
        os.mkdir(db_dir)
        shutil.copyfile("test/reset/db.json", f"{db_dir}{db_name}")
