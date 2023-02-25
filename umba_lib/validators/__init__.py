import typing

from marshmallow import validate, ValidationError


class IntegerValidator(validate.Validator):
    def __call__(self, value: typing.Any) -> typing.Any:
        if isinstance(value, str) and not value.isdecimal():
            raise ValidationError("%s is not an Integer" % value )


class FloatValidator(validate.Validator):
    def __call__(self, value: typing.Any) -> typing.Any:
        if isinstance(value, str) and not self.isfloat(value):
            raise ValidationError("%s is not a Float" % value )

    def isfloat(num):
        try:
            float(num)
            return True
        except ValueError:
            return False