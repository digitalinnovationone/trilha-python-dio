import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import db


class Account(db.Model):
    __tablename__ = "account"

    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    agency: Mapped[str] = mapped_column(sa.String(4))
    account_number: Mapped[str] = mapped_column(sa.String(10), unique=True)
    active: Mapped[bool] = mapped_column(sa.Boolean, default=True)
    user_id: Mapped[int] = mapped_column(sa.ForeignKey("user.id"), unique=True)

    user: Mapped["User"] = relationship(back_populates="account")  # type: ignore  # noqa: F821

    def __repr__(self) -> str:
        return f"Account(id={self.id!r}, agency={self.agency!r}, account_number={self.account_number!r})"
