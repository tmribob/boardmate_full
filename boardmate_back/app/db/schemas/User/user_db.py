from typing import List
from uuid import uuid4, UUID

from sqlalchemy import String, Text, Enum, ARRAY, UUID as SQL_UUID
from sqlalchemy.orm import Mapped, relationship, mapped_column

from app.db.init_db import Base
from app.enums.roles_enum import Roles


class UserDb(Base):
    __tablename__ = "users"

    uuid: Mapped[UUID] = mapped_column(SQL_UUID(as_uuid=True),
                                       primary_key=True,
                                       default=uuid4,
                                       index=True)
    nickname: Mapped[str] = mapped_column(String(32),
                                          index=True,
                                          unique=True)
    description: Mapped[str] = mapped_column(Text,
                                             nullable=True)
    avatar: Mapped[str] = mapped_column(String(128))
    roles: Mapped[List[Roles]] = mapped_column(ARRAY(Enum(Roles)),
                                               default=[Roles.USER])

    comments: Mapped[List["CommentDb"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )
    rates: Mapped[List["RateDb"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )
    initiated_friendships: Mapped[List["FriendDb"]] = relationship(
        back_populates="requester",
        cascade="all, delete-orphan",
        foreign_keys="FriendDb.requester_uuid"
    )
    received_friendships: Mapped[List["FriendDb"]] = relationship(
        back_populates="addressee",
        cascade="all, delete-orphan",
        foreign_keys="FriendDb.addressee_uuid"
    )
    games: Mapped[List["LikeDb"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )
    auth_data: Mapped["UserAuthDb"] = relationship(
        "UserAuthDb",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan"
    )


from app.db.schemas.User.friend_db import FriendDb
from app.db.schemas.User.user_auth_db import UserAuthDb
from app.db.schemas.comment_db import CommentDb
from app.db.schemas.rate_db import RateDb
from app.db.schemas.like_dp import LikeDb
