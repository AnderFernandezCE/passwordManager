from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from src.config import app_configs, settings
from src.auth.router import router as auth_router
from src.vault.router import router as vault_router
from src.paths import KEYFILE,CERTFILE
import time

app = FastAPI(**app_configs)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_origin_regex=settings.CORS_ORIGINS_REGEX,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return {"Hello": "World"}

@app.get("/healthcheck", include_in_schema=False)
async def healthcheck() -> dict[str, str]:
    status = settings.ENVIRONMENT 
    return {"status": status}

app.include_router(auth_router, prefix="/api/auth", tags=["Auth"])
app.include_router(vault_router, prefix="/api/vault", tags=["Vault"])

if __name__ == "__main__":
    uvicorn.run(app, host=settings.SITE_DOMAIN, port=settings.SITE_PORT, ssl_keyfile=KEYFILE, ssl_certfile=CERTFILE)
    