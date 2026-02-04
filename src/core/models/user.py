from sqlalchemy.orm import Mapped, mapped_column

from core.models.base import Base
from core.models.mixins.int_id_pk import IntIdPkMixin


class User(IntIdPkMixin, Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(unique=True)
