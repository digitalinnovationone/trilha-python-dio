from databases.interfaces import Record
from src.database import database
from src.models.account import accounts
from src.schemas.account import AccountCreate
from typing import List, Optional

class AccountService:
    async def read_all(self, limit: int, skip: int = 0, user_id: Optional[int] = None) -> List[Record]:
        query = accounts.select()
        if user_id is not None:
            query = query.where(accounts.c.user_id == user_id)
        query = query.limit(limit).offset(skip)
        return await database.fetch_all(query)

    async def create(self, account: AccountCreate, user_id: int) -> Record:
        command = accounts.insert().values(user_id=user_id, balance=account.balance)
        account_id = await database.execute(command)

        query = accounts.select().where(accounts.c.id == account_id)
        return await database.fetch_one(query)
