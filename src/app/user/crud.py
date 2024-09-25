from src.app.core.base_crud import BaseCRUD
from src.app.core.database import new_session
from src.app.user.model import User, UserData


class UserService(BaseCRUD):
    model = User

    @staticmethod
    async def add_user(telegram_id: int, username: str, firstname: str, lastname: str):
        async with new_session() as session:
            user_in_db = await session.get(User, telegram_id)
            if not user_in_db:
                new_user = User(
                    id=telegram_id,
                )
                session.add(new_user)

                new_user_data = UserData(
                    user_id=telegram_id,
                    username=username,
                    firstname=firstname,
                    lastname=lastname,
                )
                session.add(new_user_data)

                await session.flush()
                await session.commit()
