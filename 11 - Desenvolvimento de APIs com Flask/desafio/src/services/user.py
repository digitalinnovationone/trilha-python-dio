from src.app import bcrypt
from src.models import User, db
from src.views.user import CreateUserSchema


class UserService:
    def create(self, user_data):
        create_user_schema = CreateUserSchema()
        data = create_user_schema.load(user_data)

        user = User(name=data["name"], password=bcrypt.generate_password_hash(data["password"]), email=data["email"])
        db.session.add(user)
        db.session.commit()

        return user

    def list_all(self):
        query = db.select(User).where(User.active.is_(True))
        return db.session.execute(query).scalars()
