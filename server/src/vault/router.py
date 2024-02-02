from fastapi import APIRouter, BackgroundTasks, Depends, Response, status, Query
from src.vault.dependencies import valid_user_token
from src.vault import services
from src.vault.schemas import PasswordsResponse, CipherData, CreateItemRequest

router = APIRouter()

@router.get("/", status_code=status.HTTP_200_OK)
async def home(token:str = Depends(valid_user_token)) -> dict[str, str]:
    return {"vault" :  token}

@router.post("/create-item", status_code=status.HTTP_201_CREATED, response_model=CipherData)
async def create_item(item: CreateItemRequest, user_token:str = Depends(valid_user_token)) -> CipherData:
    created_item = await services.create_item(item,user_token)
    return created_item

@router.post("/get-passwords", status_code=status.HTTP_200_OK, response_model=PasswordsResponse)
async def get_password(user_token:str = Depends(valid_user_token)) -> PasswordsResponse:
    passwords = await services.get_passwords(user_token)
    return passwords

    