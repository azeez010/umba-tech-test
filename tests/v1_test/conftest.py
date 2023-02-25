import json, pytest

from main import app as main_app
from settings.config import create_app
from umba_lib.models import ModelUtilities
from faker_sqlalchemy import SqlAlchemyProvider, Faker

from app.v1.users.models import User


@pytest.fixture()
def app():
    ModelUtilities.start()
    app = create_app(True)
    yield app
    ModelUtilities.drop()


@pytest.fixture()
def fake_user():
    fake = Faker()
    fake.add_provider(SqlAlchemyProvider)

    return fake.sqlalchemy_model(User)


@pytest.fixture()
def client():
    return main_app.test_client()


@pytest.fixture()
def account(app, login, client) -> tuple[dict, str]:
    response = client.post("/api/v1/account/", headers={
        "Authorization": "Bearer %s" % login
    })
    return json.loads(response.data.decode('utf-8')), login


@pytest.fixture()
def user(app, client) -> dict:
    response = client.post("/api/v1/user/", data={
        "email": "azeez1@gmail.com",
        "password": "azeezlab",
        "first_name": "hello",
        "last_name": "hi",
        "phone_number": "09123456789"
    })

    return json.loads(response.data.decode('utf-8'))


@pytest.fixture()
def login(app, user, client) -> str:
    response = client.post("/api/v1/auth/login", data={
        "email": "azeez1@gmail.com",
        "password": "azeezlab"
    })
    if response:
        token_response = json.loads(response.data.decode('utf-8'))
        return token_response.get("token")
    return ""


