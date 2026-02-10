import uvicorn
from app.config.settings import settings

if __name__ == "__main__":
    uvicorn.run(
        "app.app_start:app",  
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        reload=True
    )
