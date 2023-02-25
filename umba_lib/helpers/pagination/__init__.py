from typing import Callable
from flask_sqlalchemy.pagination import QueryPagination
from marshmallow_sqlalchemy.schema import SQLAlchemySchema


class Pagination:
    @staticmethod
    def get_paginated_data(paginated_model, model_serializer: Callable) -> dict:
        model_serializer_object = model_serializer()

        if not isinstance(model_serializer_object, SQLAlchemySchema):
            raise TypeError("Object must be instance of 'marshmallow_sqlalchemy.schema.SQLAlchemySchema'")

        data = model_serializer_object.dump(paginated_model, many=True)

        if isinstance(paginated_model, QueryPagination):
            return {
                "page": paginated_model.page,
                'pages': paginated_model.pages,
                'count': paginated_model.total,
                'prev_page': paginated_model.prev_num,
                'next_page': paginated_model.next_num,
                'has_next': paginated_model.has_next,
                'has_prev': paginated_model.has_prev,
                "result": data

            }
        return data
