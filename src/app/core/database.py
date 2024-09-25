from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from src.app.settings import load_config

settings = load_config()


engine = create_async_engine(
    url=settings.database.db_url
    # echo=True
)

new_session = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=True
)
