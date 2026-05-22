import enum


class TokensTypes(str, enum.Enum):
    ACCESS = "access"
    REFRESH = "refresh"
