from uuid import uuid4, UUID

from sqlalchemy import SmallInteger, ForeignKey, UUID as SQL_UUID
from sqlalchemy.orm import Mapped, relationship, mapped_column

from app.db.init_db import Base


class RateDb(Base):
    __tablename__ = "rates"

    uuid: Mapped[UUID] = mapped_column(SQL_UUID(as_uuid=True),
                                       primary_key=True,
                                       default=uuid4,
                                       index=True)
    rate: Mapped[int] = mapped_column(SmallInteger)

    game_uuid: Mapped[UUID] = mapped_column(SQL_UUID(as_uuid=True),
                                            ForeignKey('games.uuid'))
    user_uuid: Mapped[UUID] = mapped_column(SQL_UUID(as_uuid=True),
                                            ForeignKey('users.uuid'))

    game: Mapped["GameDb"] = relationship(back_populates='rates')
    user: Mapped["UserDb"] = relationship(back_populates='rates')


from app.db.schemas.Game.game_db import GameDb
from app.db.schemas.User.user_db import UserDb
