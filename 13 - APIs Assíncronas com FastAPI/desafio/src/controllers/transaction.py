from fastapi import APIRouter, Depends, status, HTTPException
from typing import Annotated

from src.schemas.transaction import TransactionIn
from src.security import login_required, get_current_user
from src.services.transaction import TransactionService
from src.views.transaction import TransactionOut

router = APIRouter(prefix="/transactions", dependencies=[Depends(login_required)])

service = TransactionService()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TransactionOut)
async def create_transaction(transaction: TransactionIn, current_user: Annotated[dict, Depends(get_current_user)] = Depends(get_current_user)):
    user_id = current_user["user_id"]
    return await service.create(transaction, user_id=user_id)
