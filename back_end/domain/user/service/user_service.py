from back_end.domain.user.dto.request.user_create_dto import UserCreateDto
from back_end.domain.user.dto.response.user_response import UserResponse
from back_end.domain.user.repository.user_repository import UserRepository


class UserService:


    def __init__(self, user_repository: UserRepository):

        self.user_repository = user_repository

    def register_user(self, dto: UserCreateDto) -> UserResponse:
        """
        [비지니스 로직]
        1. 아이디 중복 체크
        2. DTO 데이터 기반으로 User 엔티티 생성(비밀번호 암호화등)
        3. 레포지토리를 통해 저장
        4. 결과를 UserResponse로 변환하여 반환
        """
        existing_user = self.user_repository.find_by_id(dto.user_id)
        if existing_user is not None:
            raise ValueError(f"이미 존재하는 아이디입니다. : {dto.user_id}")

        new_user = dto.to_entity()

        saved_user = self.user_repository.save(new_user)

        return UserResponse.from_entity(saved_user)

    def withdraw_user(self, user_id: str) -> bool:

        existing_user = self.user_repository.find_by_id(user_id)
        if existing_user is None:
            raise ValueError(f"{user_id}는 존재하지 않습니다.")

        return self.user_repository.delete(user_id)