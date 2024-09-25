from sqlalchemy import BIGINT, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.app.core.base_model import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    role: Mapped[str] = mapped_column(default="user")
    is_banned: Mapped[bool] = mapped_column(default=False)

    data: Mapped[int] = relationship("UserData", back_populates="user")


class UserData(Base):
    __tablename__ = "user_datas"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)
    username: Mapped[str] = mapped_column(nullable=True)
    firstname: Mapped[str] = mapped_column(nullable=True)
    lastname: Mapped[str] = mapped_column(nullable=True)

    user: Mapped[int] = relationship("User", back_populates="data")
