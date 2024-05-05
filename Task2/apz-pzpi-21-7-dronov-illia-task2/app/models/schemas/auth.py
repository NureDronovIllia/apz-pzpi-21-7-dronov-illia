from pydantic import BaseModel, EmailStr, field_validator

# from app.models.schemas.users import UserBase
from app.utilities.validators.payload.user import (
    validate_passport_number,
    validate_password,
)


# class ClientSignUpInput(UserBase):
#     password: str

#     @field_validator("password")
#     @classmethod
#     def validate_password(cls, value):
#         return validate_password(value)


# class AdminInput(BaseModel):
#     email: EmailStr
#     password: str

#     @field_validator("password")
#     @classmethod
#     def validate_password(cls, value):
#         return validate_password(value)


# class ClientSchema(UserBase):
#     id: int

#     class Config:
#         from_attributes: True


# class DriverSignUpInput(UserBase):
#     password: str
#     driver_license_number: str
#     passport_number: str

#     @field_validator("password")
#     @classmethod
#     def validate_password(cls, value):
#         return validate_password(value)

#     @field_validator("driver_license_number")
#     @classmethod
#     def validate_driver_license_number(cls, value):
#         return validate_driver_license_number(value)

#     @field_validator("passport_number")
#     @classmethod
#     def validate_passport_number(cls, value):
#         return validate_passport_number(value)


# class UserSignUpOutput(BaseModel):
#     id: int
#     email: EmailStr


# class UserLoginInput(BaseModel):
#     email: EmailStr
#     password: str


# class UserLoginOutput(BaseModel):
#     token: str
