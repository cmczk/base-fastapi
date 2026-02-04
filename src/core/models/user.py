from sqlalchemy.orm import Mapped, mapped_column

from core.models.base import Base


class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(unique=True)
