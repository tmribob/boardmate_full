from uuid import uuid4, UUID

from sqlalchemy import ForeignKey, UUID as SQL_UUID
from sqlalchemy.orm import Mapped, relationship, mapped_column

from app.db.init_db import Base


class GameGenreDb(Base):
    __tablename__ = "game_genre"

    uuid: Mapped[UUID] = mapped_column(SQL_UUID(as_uuid=True),
                                       primary_key=True,
                                       default=uuid4,
                                       index=True)

    genre_uuid: Mapped[UUID] = mapped_column(SQL_UUID(as_uuid=True),
                                             ForeignKey('genres.uuid'))
    game_uuid: Mapped[UUID] = mapped_column(SQL_UUID(as_uuid=True),
                                            ForeignKey('games.uuid'))

    genre: Mapped["GenreDb"] = relationship(back_populates='games')
    game: Mapped["GameDb"] = relationship(back_populates='genres')


from app.db.schemas.Game.genre_db import GenreDb
from app.db.schemas.Game.game_db import GameDb
