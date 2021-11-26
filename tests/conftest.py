import pytest
from application.database import db
from main import app


@pytest.fixture(scope="module")
def client():
    print("**************** GETTING CLIENT ****************")
    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    client = app.test_client()

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()
    
    yield client  # this is where the testing happens!

    # Tear down
    ctx.pop()


@pytest.fixture(scope="module")
def init_database():
    # Create the database and the database table
    db.create_all()

    yield db  # this is where the testing happens!

    # Tear down
    db.drop_all()
