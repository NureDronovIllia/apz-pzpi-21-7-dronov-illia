import enum
from datetime import datetime

from sqlalchemy import TIMESTAMP, Column, Enum, Integer, String

from app.core.database import Base


class Roles(enum.Enum):
    Employee = "employee"
    Admin = "admin"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String(), nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth_date = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    passport_number = Column(String)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow())
    role = Column(Enum(Roles))

    def __repr__(self) -> str:
        return f'User "{self.first_name} {self.last_name}"'
