from typing import List
from uuid import uuid4, UUID

from sqlalchemy import String, UUID as SQL_UUID
from sqlalchemy.orm import Mapped, relationship, mapped_column

from app.db.init_db import Base


class DifficultyDb(Base):
    __tablename__ = "difficulties"

    uuid: Mapped[UUID] = mapped_column(SQL_UUID(as_uuid=True),
                                       primary_key=True,
                                       default=uuid4,
                                       index=True)
    name: Mapped[str] = mapped_column(String(128),
                                      unique=True)

    games: Mapped[List["GameDb"]] = relationship(back_populates='difficulty')


from app.db.schemas.Game.game_db import GameDb
