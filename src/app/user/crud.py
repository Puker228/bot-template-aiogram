from src.app.user.schema import UserCreateSchema
from src.core.base_crud import BaseCRUD
from src.core.database import new_session
from src.app.user.model import User, UserData


class UserService(BaseCRUD):
    model = User

    @staticmethod
    async def add_user(user_data: UserCreateSchema):
        async with new_session() as session:
            user_in_db = await session.get(User, user_data.telegram_id)
            if not user_in_db:
                new_user = User(
                    id=user_data.telegram_id,
                )
                session.add(new_user)

                new_user_data = UserData(
                    user_id=user_data.telegram_id,
                    username=user_data.username,
                    firstname=user_data.firstname,
                    lastname=user_data.lastname,
                )
                session.add(new_user_data)

                await session.flush()
                await session.commit()
