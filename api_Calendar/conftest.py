from shutil import copy
import pytest
from api_Calendar.api import create_app
from api_Calendar.constants import API_CALENDAR_DATABASE, PROJECT_ROOT

#initialize the test
@pytest.fixture
def client(tmpdir):
    copy(f"{PROJECT_ROOT}/{API_CALENDAR_DATABASE}", tmpdir.dirpath())

    temp_db_file = f"sqlite:///{tmpdir.dirpath()}/{API_CALENDAR_DATABASE}"

    app = create_app(temp_db_file)
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client