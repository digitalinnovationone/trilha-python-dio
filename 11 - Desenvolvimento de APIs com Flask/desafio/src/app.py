import os
from http import HTTPStatus

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask import Flask, json
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import HTTPException

from src.models import db

migrate = Migrate()
bcrypt = Bcrypt()
ma = Marshmallow()
spec = APISpec(
    title="DIO Challenge",
    version="1.0.0",
    openapi_version="3.0.3",
    info=dict(description="DIO Challenge"),
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)


def create_app(environment=os.environ["ENVIRONMENT"]):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(f"src.config.{environment.title()}Config")

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    ma.init_app(app)

    # register blueprints
    from src.controllers import account, user

    app.register_blueprint(user.app)
    app.register_blueprint(account.app)

    @app.route("/docs")
    def docs():
        return spec.path(view=user.create_user).path(view=user.list_users).path(view=account.create_account).to_dict()

    @app.errorhandler(IntegrityError)
    def handle_integrity_exception(e):
        _exc = HTTPException(str(e.orig))
        _exc.code = HTTPStatus.CONFLICT
        return handle_exception(_exc)

    @app.errorhandler(HTTPException)
    def handle_exception(e):
        """Return JSON instead of HTML for HTTP errors."""
        response = e.get_response()
        response.data = json.dumps(
            {
                "code": e.code,
                "name": e.name,
                "description": e.description,
            }
        )
        response.content_type = "application/json"
        return response

    return app
