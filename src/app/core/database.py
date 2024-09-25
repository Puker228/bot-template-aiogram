from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from src.app.settings import settings

engine = create_async_engine(
    settings.DATABASE_URL,
    # echo=True
)

new_session = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=True
)
