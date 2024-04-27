from src.models import Account, db
from src.views.account import CreateAccountSchema


class AccountService:
    def create(self, account_data):
        create_account_schema = CreateAccountSchema()
        data = create_account_schema.load(account_data)

        account = Account(
            agency=data["agency"],
            account_number=data["account_number"],
            user_id=data["user_id"],
        )
        db.session.add(account)
        db.session.commit()

        return account
