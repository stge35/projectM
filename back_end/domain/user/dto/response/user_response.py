from dataclasses import dataclass

from back_end.domain.user.dto.user_dto import UserDto

@dataclass
class UserResponse:
    user_id: str
    user_pw: str
    user_name: str
    user_phone_number: str
    user_personal_number: str

    @classmethod
    def from_user_dto(cls, dto: UserDto) -> "UserResponse":

        return cls(
            user_id = cls.user_id,
            user_pw = cls.user_pw,
            user_name = cls.user_name,
            user_phone_number = cls.user_phone_number,
            user_personal_number = cls.user_personal_number
        )