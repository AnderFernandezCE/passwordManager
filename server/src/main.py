from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from src.config import app_configs, settings


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
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host=settings.SITE_DOMAIN, port=settings.SITE_PORT)
    