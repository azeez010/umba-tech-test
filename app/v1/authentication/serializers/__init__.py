from apiflask import Schema
from apiflask.fields import String
from apiflask.validators import Length, Email


class LoginSchema(Schema):
    email = String(required=True, validate=Email())
    password = String(required=True, validate=Length(8, 40))
    