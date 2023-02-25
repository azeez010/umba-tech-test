from apiflask import Schema
from apiflask.fields import String


class TokenAuthSchema(Schema):
    Authorization = String(required=True)
