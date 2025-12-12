from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

from src.schemas.account import AccountCreate
from src.security import login_required, get_current_user
from src.services.account import AccountService
from src.services.transaction import TransactionService
from src.views.account import AccountOut, TransactionOut

router = APIRouter(prefix="/accounts", dependencies=[Depends(login_required)])

account_service = AccountService()
tx_service = TransactionService()

@router.get("/", response_model=list[AccountOut])
async def read_accounts(limit: int, skip: int = 0, current_user: Annotated[dict, Depends(get_current_user)] = Depends(get_current_user)):
    user_id = current_user["user_id"]
    return await account_service.read_all(limit=limit, skip=skip, user_id=user_id)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=AccountOut)
async def create_account(account: AccountCreate, current_user: Annotated[dict, Depends(get_current_user)] = Depends(get_current_user)):
    user_id = current_user["user_id"]
    return await account_service.create(account, user_id=user_id)


@router.get("/{id}/transactions", response_model=list[TransactionOut])
async def read_account_transactions(id: int, limit: int, skip: int = 0, current_user: Annotated[dict, Depends(get_current_user)] = Depends(get_current_user)):
    user_id = current_user["user_id"]
    # garantir que a conta pertence ao user
    accounts = await account_service.read_all(limit=1, skip=0, user_id=user_id)
    # verificar existência de conta com id
    query_account = next((a for a in accounts if a["id"] == id), None)
    if not query_account:
        raise HTTPException(status_code=404, detail="Account not found")
    return await tx_service.read_all(account_id=id, limit=limit, skip=skip)
