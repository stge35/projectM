from dataclasses import dataclass
from back_end.domain.user.entity.user import User

'''
유저 가입을 위한 dto
'''
@dataclass
class UserCreateDto:
    user_id: str
    user_pw: str
    user_name: str
    user_personal_number: str
    user_phone_number: str | None

    def to_entity(self) -> User:
        return User(
            user_id = self.user_id,
            user_pw = self.user_pw,
            user_name = self.user_name,
            user_personal_number = self.user_personal_number,
            user_phone_number = self.user_phone_number
        )

