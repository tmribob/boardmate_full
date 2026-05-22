from uuid import uuid4, UUID

from sqlalchemy import Text, ForeignKey, UUID as SQL_UUID
from sqlalchemy.orm import Mapped, relationship, mapped_column

from app.db.init_db import Base


class CommentDb(Base):
    __tablename__ = "comments"

    uuid: Mapped[UUID] = mapped_column(SQL_UUID(as_uuid=True),
                                       primary_key=True,
                                       default=uuid4,
                                       index=True)
    context: Mapped[str] = mapped_column(Text)

    game_uuid: Mapped[UUID] = mapped_column(SQL_UUID(as_uuid=True),
                                            ForeignKey('games.uuid'))
    user_uuid: Mapped[UUID] = mapped_column(SQL_UUID(as_uuid=True),
                                            ForeignKey('users.uuid'))

    game: Mapped["GameDb"] = relationship(back_populates='comments')
    user: Mapped["UserDb"] = relationship(back_populates='comments')


from app.db.schemas.Game.game_db import GameDb
from app.db.schemas.User.user_db import UserDb
