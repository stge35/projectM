from __future__ import annotations
from dataclasses import dataclass

from back_end.domain.user.entity.user import User

'''
"UserDto" 의 효과 
"'''

# 이 Dto의 용도에 대해서 정확히 할것!

@dataclass
class UserDto:
    user_id: str
    user_pw: str
    user_name: str
    user_phone_number: str
    user_personal_number: str

    @classmethod
    def of(cls, dto: User) -> "UserDto":

        return cls(
            user_id = dto.user_id,
            user_pw = dto.user_pw,
            user_name = dto.user_name,
            user_phone_number = dto.user_phone_number,
            user_personal_number = dto.user_personal_number
        )