from sqlalchemy import select

from src.app.core.database import new_session


class BaseCRUD:
    model = None

    @classmethod
    async def find_all(cls, **filter_by):
        async with new_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with new_session() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.mappings().one_or_none()
