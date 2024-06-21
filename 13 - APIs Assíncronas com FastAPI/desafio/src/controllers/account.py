from fastapi import APIRouter, Depends, status

from src.schemas.account import AccountIn
from src.security import login_required
from src.services.account import AccountService
from src.services.transaction import TransactionService
from src.views.account import AccountOut, TransactionOut

router = APIRouter(prefix="/accounts", dependencies=[Depends(login_required)])

account_service = AccountService()
tx_service = TransactionService()


@router.get("/", response_model=list[AccountOut])
async def read_accounts(limit: int, skip: int = 0):
    return await account_service.read_all(limit=limit, skip=skip)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=AccountOut)
async def create_account(account: AccountIn):
    return await account_service.create(account)


@router.get("/{id}/transactions", response_model=list[TransactionOut])
async def read_account_transactions(id: int, limit: int, skip: int = 0):
    return await tx_service.read_all(account_id=id, limit=limit, skip=skip)
