from uuid import uuid4, UUID

from sqlalchemy import ForeignKey, Enum, UUID as SQL_UUID
from sqlalchemy.orm import Mapped, relationship, mapped_column

from app.db.init_db import Base
from app.enums.friendship_enum import FriendshipStatus


class FriendDb(Base):
    __tablename__ = "friends"

    uuid: Mapped[UUID] = mapped_column(SQL_UUID(as_uuid=True),
                                       primary_key=True,
                                       default=uuid4
                                       )
    requester_uuid: Mapped[UUID] = mapped_column(SQL_UUID(as_uuid=True),
                                                 ForeignKey('users.uuid'),
                                                 index=True)
    addressee_uuid: Mapped[UUID] = mapped_column(SQL_UUID(as_uuid=True),
                                                 ForeignKey('users.uuid'),
                                                 index=True)
    status: Mapped[FriendshipStatus] = mapped_column(Enum(FriendshipStatus),
                                                     default=FriendshipStatus.PENDING)

    requester: Mapped["UserDb"] = relationship(
        back_populates="initiated_friendships",
        foreign_keys=[requester_uuid]
    )
    addressee: Mapped["UserDb"] = relationship(
        back_populates="received_friendships",
        foreign_keys=[addressee_uuid]
    )


from app.db.schemas.User.user_db import UserDb
