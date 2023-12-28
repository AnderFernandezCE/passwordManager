from fastapi import APIRouter, BackgroundTasks, Depends, Response, status, Query

from src.auth.schemas import RegisterRequest, RegisterResponse
from src.auth.dependencies import valid_register_user
from src.auth import services

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
async def fetch_memories() -> dict[str, str]:
    return {"auth" :  "router"}

@router.post("/login", status_code=status.HTTP_200_OK)
async def login() -> dict[str, str]:
    return {"auth" :  "login"}

@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=RegisterResponse)
async def register(user_request : RegisterRequest  = Depends(valid_register_user)) -> RegisterResponse:
    # services.register(user_request) # todo
    return RegisterResponse(**user_request.user.dict())

# TOKENS/SESSIONS REFRESH
    
    