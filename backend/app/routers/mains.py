from fastapi import APIRouter
from fastapi.responses import FileResponse

from app.schemas.sch_main import Status

router = APIRouter(
    tags=["API MAIN"]
)

@router.get("/")
async def status():
    """STATUS app"""
    return Status()

@router.get("/favicon.ico")
async def favicon():
    """FAVICON INIT app"""
    return FileResponse("app/static/favicon.ico")