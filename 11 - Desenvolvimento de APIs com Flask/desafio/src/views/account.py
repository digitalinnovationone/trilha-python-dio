from marshmallow import fields

from src.app import ma
from src.models.account import Account


class AccountSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Account

    id = ma.auto_field()
    agency = ma.auto_field()
    account_number = ma.auto_field()
    active = ma.auto_field()


class CreateAccountSchema(ma.Schema):
    agency = fields.String(required=True)
    account_number = fields.String(required=True)
    user_id = fields.Integer(required=True, strict=True)
