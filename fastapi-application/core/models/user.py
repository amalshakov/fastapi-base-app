from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from .base import Base
from .mixins.id_int_pk import IdIntPkMixin


class User(IdIntPkMixin, Base):
    username: Mapped[str] = mapped_column(unique=True)
    foo: Mapped[int]
    bar: Mapped[int]

    __table_args__ = (UniqueConstraint("foo", "bar"),)
