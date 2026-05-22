from typing import List
from uuid import uuid4, UUID

from sqlalchemy import String, Text, SmallInteger, ForeignKey, UUID as SQL_UUID
from sqlalchemy.orm import Mapped, relationship, mapped_column

from app.db.init_db import Base


class GameDb(Base):
    __tablename__ = "games"

    uuid: Mapped[UUID] = mapped_column(SQL_UUID(as_uuid=True),
                                       primary_key=True,
                                       default=uuid4,
                                       index=True)
    name: Mapped[str] = mapped_column(String(128),
                                      unique=True)
    description: Mapped[str] = mapped_column(Text,
                                             nullable=True)
    photo: Mapped[str] = mapped_column(String(128))

    min_players: Mapped[int] = mapped_column(SmallInteger)
    max_players: Mapped[int] = mapped_column(SmallInteger)

    min_duration: Mapped[int] = mapped_column(SmallInteger)
    max_duration: Mapped[int] = mapped_column(SmallInteger)

    difficulty_uuid: Mapped[UUID] = mapped_column(SQL_UUID(as_uuid=True),
                                                  ForeignKey("difficulties.uuid"))

    difficulty: Mapped["DifficultyDb"] = relationship(
        back_populates="games"
    )
    genres: Mapped[List["GameGenreDb"]] = relationship(
        back_populates="game",
        cascade="all, delete-orphan"
    )
    comments: Mapped[List["CommentDb"]] = relationship(
        back_populates="game",
        cascade="all, delete-orphan"
    )
    rates: Mapped[List["RateDb"]] = relationship(
        back_populates="game",
        cascade="all, delete-orphan"
    )
    users: Mapped[List["LikeDb"]] = relationship(
        back_populates="game"
    )


from app.db.schemas.Game.difficulty_db import DifficultyDb
from app.db.schemas.Game.game_genre_db import GameGenreDb
from app.db.schemas.like_dp import LikeDb
from app.db.schemas.comment_db import CommentDb
from app.db.schemas.rate_db import RateDb
