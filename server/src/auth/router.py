from fastapi import APIRouter, BackgroundTasks, Depends, Response, status, Query

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
async def fetch_memories() -> dict[str, str]:
    return {"auth" :  "router"}

@router.get("/login", status_code=status.HTTP_200_OK)
async def fetch_memories() -> dict[str, str]:
    return {"auth" :  "login"}

@router.get("/register", status_code=status.HTTP_200_OK)
async def fetch_memories() -> dict[str, str]:
    return {"auth" :  "register"}


    
    