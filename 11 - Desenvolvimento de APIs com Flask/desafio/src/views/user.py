from marshmallow import fields

from src.app import ma
from src.models.user import User
from src.views.account import AccountSchema


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    name = ma.auto_field()
    email = ma.auto_field()
    account = ma.Nested(AccountSchema)


class CreateUserSchema(ma.Schema):
    name = fields.String(required=True)
    password = fields.String(required=True)
    email = fields.Email(required=True)
