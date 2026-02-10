from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from app.config.settings import settings

DATABASE_URL = settings.get_db_url()

engine = create_async_engine(settings.DATABASE_URL, echo=True)

AsyncSessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False,
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
