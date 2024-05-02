from datetime import datetime

from pydantic import BaseModel, EmailStr, field_validator

from app.models.db.users import Roles
from app.utilities.validators.payload.datetime import validate_date_format
from app.utilities.validators.payload.user import validate_name, validate_phone_number


class UserBase(BaseModel):
    first_name: str
    last_name: str
    birth_date: str
    email: EmailStr
    phone_number: str

    @field_validator("first_name")
    @classmethod
    def validate_first_name(cls, value):
        return validate_name(value, "first_name")

    @field_validator("last_name")
    @classmethod
    def validate_last_name(cls, value):
        return validate_name(value, "last_name")

    @field_validator("birth_date")
    @classmethod
    def validate_birth_date(cls, value):
        return validate_date_format(value, "birth_date")

    @field_validator("phone_number")
    @classmethod
    def validate_user_phone_number(cls, value):
        return validate_phone_number(value)


class DriverSchema(UserBase):
    id: int
    driver_license_number: str
    passport_number: str
    registered_at: datetime
    role: Roles

    class Config:
        from_attributes = True
