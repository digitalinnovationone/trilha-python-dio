from http import HTTPStatus

from flask import Blueprint, request
from marshmallow import ValidationError

from src.services.user import UserService
from src.views.user import UserSchema

app = Blueprint("user", __name__, url_prefix="/users")


@app.route("/")
def list_users():
    """User list view.
    ---
    get:
      tags:
        - user
      summary: List active users
      responses:
        200:
          description: Successful operation
          content:
            application/json:
              schema:
                type: array
                items: UserSchema
    """
    service = UserService()
    users_schema = UserSchema(many=True)
    return users_schema.dump(service.list_all())


@app.route("/", methods=["POST"])
def create_user():
    """User create view.
    ---
    post:
      tags:
        - user
      summary: Add a new user
      requestBody:
        description: Create a new user in the bank
        content:
          application/json:
            schema: CreateUserSchema
        required: true
      responses:
        201:
          description: Successful operation
          content:
            application/json:
              schema: UserSchema
    """
    user_schema = UserSchema()
    service = UserService()

    try:
        user = service.create(user_data=request.json)
    except ValidationError as exc:
        return exc.messages, HTTPStatus.UNPROCESSABLE_ENTITY

    return user_schema.dump(user), HTTPStatus.CREATED
