from settings.database import ma
from app.v1.users.models import User
from marshmallow import fields, validate
from umba_lib.validators import IntegerValidator


class UserSchema:
    class Create(ma.SQLAlchemyAutoSchema):
        phone_number = fields.Str(required=True, validate=[validate.Length(equal=11), IntegerValidator()])
        email = fields.Str(required=True, validate=[validate.Email()])
        password = fields.Str(required=True, validate=[validate.Length(min=8)])

        class Meta:
            exclude = ("accounts", "id")
            model = User

    class Retrieve(ma.SQLAlchemyAutoSchema):
        class Meta:
            exclude = ("accounts", "password")
            model = User

    class Update(ma.SQLAlchemyAutoSchema):
        phone_number = fields.Str(required=False, validate=[validate.Length(equal=11), IntegerValidator()])
        email = fields.Str(required=False, validate=[validate.Email()])
        password = fields.Str(required=False, validate=[validate.Length(min=8)])
        first_name = fields.Str(required=False)
        last_name = fields.Str(required=False)

        class Meta:
            exclude = ("accounts", "id")
            model = User
