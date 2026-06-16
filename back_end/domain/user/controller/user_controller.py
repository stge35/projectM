from back_end.domain.user.dto.request.user_create_dto import UserCreateDto
from back_end.domain.user.dto.response.user_response import UserResponse
from back_end.domain.user.service.user_service import UserService


class UserController:

    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def signup(self, dto: UserCreateDto) -> UserResponse:

        try:
            response: UserResponse = self.user_service.register_user(dto)
            return response

        except ValueError as e:
            raise ValueError(f"등록실패")
