from uuid import uuid4, UUID

from sqlalchemy import ForeignKey, UUID as SQL_UUID
from sqlalchemy.orm import Mapped, relationship, mapped_column

from app.db.init_db import Base


class LikeDb(Base):
    __tablename__ = "likes"

    uuid: Mapped[UUID] = mapped_column(SQL_UUID(as_uuid=True),
                                       primary_key=True,
                                       default=uuid4,
                                       index=True)
    user_uuid: Mapped[UUID] = mapped_column(SQL_UUID(as_uuid=True),
                                            ForeignKey('users.uuid'))
    game_uuid: Mapped[UUID] = mapped_column(SQL_UUID(as_uuid=True),
                                            ForeignKey('games.uuid'))

    user: Mapped["UserDb"] = relationship(
        back_populates='games',
    )
    game: Mapped["GameDb"] = relationship(
        back_populates='users',
    )


from app.db.schemas.User.user_db import UserDb
from app.db.schemas.Game.game_db import GameDb
