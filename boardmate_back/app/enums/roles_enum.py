import enum


class Roles(str, enum.Enum):
    USER = "user"
    ADMIN = "admin"
