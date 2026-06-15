from dataclasses import dataclass


@dataclass
class User:
    user_id: str
    user_pw: str
    user_name: str
    user_phone_number: str
    user_personal_number: str

