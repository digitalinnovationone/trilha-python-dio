import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import db


class User(db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    email: Mapped[str] = mapped_column(sa.String, unique=True, nullable=False)
    name: Mapped[str] = mapped_column(sa.String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(sa.String, nullable=False)
    active: Mapped[bool] = mapped_column(sa.Boolean, default=True)

    account: Mapped["Account"] = relationship(back_populates="user", uselist=False)  # type: ignore  # noqa: F821

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, email={self.email!r})"
