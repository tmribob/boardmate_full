from typing import Optional
from uuid import uuid4, UUID

from sqlalchemy import String, ForeignKey, UUID as SQL_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.init_db import Base


class UserAuthDb(Base):
    __tablename__ = "usersAuth"

    uuid: Mapped[UUID] = mapped_column(SQL_UUID(as_uuid=True),
                                       primary_key=True,
                                       default=uuid4,
                                       index=True)
    email: Mapped[str] = mapped_column(String(128),
                                       unique=True,
                                       index=True)
    password: Mapped[str] = mapped_column(String(164))
    current_refresh: Mapped[Optional[str]] = mapped_column(String,
                                                           nullable=True,
                                                           unique=True)
    user_uuid: Mapped[UUID] = mapped_column(SQL_UUID(as_uuid=True),
                                            ForeignKey("users.uuid",
                                                       ondelete="CASCADE"),
                                            unique=True)

    user: Mapped["UserDb"] = relationship("UserDb",
                                          back_populates="auth_data")


from app.db.schemas.User.user_db import UserDb
