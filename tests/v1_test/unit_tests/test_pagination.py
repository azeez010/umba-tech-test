from app.v1.users.models import User
from app.v1.users.serializers import UserSchema
from umba_lib.helpers.pagination import Pagination
from umba_lib.models import ModelUtilities
from settings.config import app as app_setting


class TestPagination:
    def test_pagination(self, app):
        with app_setting.app_context():
            ModelUtilities.create(User, first_name="az", email="d22222@gmail.com", phone_number="08142700831", password="azeez111")
            paginated_data = Pagination.get_paginated_data(ModelUtilities.list(User, page=1, per_page=1), UserSchema.Retrieve)

            assert paginated_data.get("page") == 1