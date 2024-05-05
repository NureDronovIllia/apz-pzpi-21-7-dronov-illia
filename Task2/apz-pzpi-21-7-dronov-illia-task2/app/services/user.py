# from typing import Any
# from fastapi import HTTPException, status
# from sqlalchemy.exc import IntegrityError

# from app.config.logs.logger import logger
# from app.models.db.user import User
# from app.models.schemas.auth import (
#     ClientSchema,
#     ClientSignUpInput,
#     DriverSignUpInput,
#     UserLoginInput,
#     UserLoginOutput,
#     UserSignUpOutput,
# )
# from app.models.schemas.users import DriverSchema
from app.repository.user import UserRepository
from app.securities.authorization.auth_handler import auth_handler
from app.services.base import BaseService
from app.utilities.formatters.http_error import error_wrapper


class UserService(BaseService):
    def __init__(self, user_repository) -> None:
        self.user_repository: UserRepository = user_repository

    # async def _register_user(
    #     self,
    #     user_data: ClientSignUpInput | DriverSignUpInput,
    #     model_create_class: Any
    # ) -> UserSignUpOutput:
    #     # Hashing input password
    #     user_data.password = auth_handler.get_password_hash(user_data.password)

    #     try:
    #         result = await self.user_repository.create_user(
    #             model_create_class(**user_data.model_dump())
    #         )
    #     except IntegrityError:
    #         raise HTTPException(
    #             status.HTTP_409_CONFLICT,
    #             detail=error_wrapper("User with this email already exists", "email"),
    #         )

    #     logger.info("New user instance has been successfully created")
    #     return result

    # async def get_drivers(self, current_user_id: int) -> list[DriverSchema]:
    #     await self._validate_user_permissions(
    #         self.user_repository, current_user_id, Roles.Admin
    #     )
    #     return await self.user_repository.get_drivers()

    # async def get_clients(self, current_user_id: int) -> list[ClientSchema]:
    #     await self._validate_user_permissions(
    #         self.user_repository, current_user_id, Roles.Admin
    #     )
    #     return await self.user_repository.get_clients()

    # async def register_client(self, user_data: ClientSignUpInput) -> UserSignUpOutput:
    #     return await self._register_user(user_data, ClientModelCreate)

    # async def register_driver(self, user_data: DriverSignUpInput) -> UserSignUpOutput:
    #     return await self._register_user(user_data, DriverModelCreate)

    # async def authenticate_user(self, user_data: UserLoginInput) -> UserLoginOutput:
    #     logger.info(f'Login attempt with email "{user_data.email}"')

    #     user_existing_object: User = await self.user_repository.get_user_by_email(
    #         user_data.email
    #     )
    #     if not user_existing_object:
    #         logger.warning(
    #             f'User with email "{user_data.email}" is not registered in the system'
    #         )
    #         raise HTTPException(
    #             status.HTTP_404_NOT_FOUND,
    #             detail="User with this email is not registered in the system",
    #         )

    #     verify_password = auth_handler.verify_password(
    #         user_data.password, user_existing_object.password
    #     )
    #     if not verify_password:
    #         logger.warning("Invalid password was provided")
    #         raise HTTPException(
    #             status.HTTP_400_BAD_REQUEST,
    #             detail=error_wrapper("Invalid password", "password"),
    #         )

    #     logger.info(f'User "{user_data.email}" successfully logged in the system')
    #     auth_token = auth_handler.encode_token(user_existing_object.id, user_data.email)
    #     return {"token": auth_token}

    # async def get_pending_drivers(self, current_user_id: int) -> list[DriverSchema]:
    #     await self._validate_user_permissions(
    #         self.user_repository, current_user_id, Roles.Admin
    #     )

    #     return await self.user_repository.get_pending_drivers()

    # async def export_data_xlsx(self, current_user_id):
    #     await self._validate_user_permissions(
    #         self.user_repository, current_user_id, Roles.Admin
    #     )
    #     return await self.user_repository.export_data_xlsx()