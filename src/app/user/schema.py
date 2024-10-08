from pydantic import BaseModel
from typing import Optional


class UserCreateSchema(BaseModel):
    telegram_id: int
    username: Optional[str]
    firstname: Optional[str]
    lastname: Optional[str]


