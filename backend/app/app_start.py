from fastapi import FastAPI

from app.routers.mains import router as my_home

app = FastAPI(
    title="Workspace API",
    version="0.1.0",
    description="APP Workspace API",
    openapi_version="3.1.0",    
    root_path="/api",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(my_home)