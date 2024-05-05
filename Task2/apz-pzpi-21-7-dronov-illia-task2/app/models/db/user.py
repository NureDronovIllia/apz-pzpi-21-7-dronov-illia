from datetime import datetime
import enum

from sqlalchemy import String, Enum
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from app.core.database import Base


class Genders(Enum):
    Male = 0
    Female = 1


class UserRoles(enum.Enum):
    EMPLOYEE = "employee"
    ADMIN = "admin" 


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    birth_data: Mapped[str] = mapped_column(String(10))
    gender: Mapped[bool]
    role: Mapped[UserRoles] = mapped_column(
        Enum(
            UserRoles,
            name="userrole",
            create_constraint=True,
            validate_strings=True,
        )
    )
    email: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(32))
    passport_number: Mapped[str] = mapped_column(String(32))
    registered_at: Mapped[datetime] = mapped_column(default=func.now())

    def __repr__(self) -> str:
        return f'User "{self.first_name} {self.last_name}"'
