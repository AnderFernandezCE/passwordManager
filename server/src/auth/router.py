from fastapi import APIRouter, BackgroundTasks, Depends, Response, status, Query
from fastapi.security import OAuth2PasswordBearer

from src.auth.schemas import RegisterRequest, RegisterResponse, UserLoginResponse, LoginRequest
from src.auth.dependencies import valid_register_user, valid_verification_token, valid_login_user, is_token_valid, is_token_valid_db
from src.auth import services

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
async def fetch_memories() -> dict[str, str]:
    return {"auth" :  "router"}

@router.post("/login", status_code=status.HTTP_200_OK, response_model=UserLoginResponse)
async def login(user_request : LoginRequest = Depends(valid_login_user)) -> UserLoginResponse:
    #create token/cookie
    refresh_token = await services.generate_refresh_token(user_request.uuid)
    user_request.refresh_token = refresh_token
    return user_request

@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=RegisterResponse)
async def register(user_request : RegisterRequest  = Depends(valid_register_user)) -> RegisterResponse:
    response = await services.register_user(user_request.user)
    return RegisterResponse(**user_request.user.dict()) #return Ok?

@router.get("/new-register", status_code=status.HTTP_200_OK)# to verify account
async def verificate(token : str  = Depends(valid_verification_token)):
    await services.verificate_user_account(token)
    return {"status": "verified" }

# TOKENS/SESSIONS REFRESH
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/get-access-token", status_code=status.HTTP_200_OK)
async def get_access_token(token: str = Depends(is_token_valid_db)):
    access_token = services.generate_access_token(token)
    return {"access_token": access_token}

@router.post("/revoke-token", status_code=status.HTTP_200_OK)
async def revoke_token(token: str = Depends(is_token_valid)):
    await services.revoke_token(token)
    return {"status": "revoked"}
    