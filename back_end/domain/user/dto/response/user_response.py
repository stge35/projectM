from dataclasses import dataclass
from back_end.domain.user.entity.user import User


@dataclass
class UserResponse:
    user_id: str
    user_name: str
    user_phone_number: str
    user_personal_number: str

    @classmethod
    def from_entity(cls, dto: User) -> "UserResponse":

        return cls(
            user_id = dto.user_id,
            user_name = dto.user_name,
            user_phone_number = dto.user_phone_number,
            user_personal_number = dto.user_personal_number
        )