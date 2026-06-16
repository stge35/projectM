import json
import os.path

from back_end.domain.user.entity.user import User
from back_end.domain.user.repository.user_repository import UserRepository


class FileUserRepository(UserRepository):

    def __init__(self, file_path: str = "users.json"):
        super().__init__(storage_path=file_path)
        if not os.path.exists(self.storage_path):
            self._save_file({})


    def save(self, user: User) -> User:
        all_users = self._read_file()

        all_users[user.user_id] = {
            "user_id": user.user_id,
            "user_pw": user.user_pw,
            "user_name": user.user_name,
            "user_personal_number": user.user_personal_number,
            "user_phone_number": user.user_phone_number
        }

        self._save_file(all_users)
        return user

    def find_by_id(self, user_id: str) -> User | None:

        all_users = self._read_file()

        if user_id not in all_users:
            return None

        data = all_users[user_id]

        return User(
            user_id=data["user_id"],
            user_pw=data["user_pw"],
            user_name=data["user_name"],
            user_personal_number=data["user_personal_number"],
            user_phone_number=data["user_phone_number"]
        )


    def delete(self, user_id: str) -> bool:
        all_users = self._read_file()

        if user_id not in all_users:
            return False

        del all_users[user_id]

        self._save_file(all_users)
        return True

    def _read_file(self) -> dict:
        with open(self.file_path, "r", encoding = "utf-8") as f:
            return json.load(f)

    def _save_file(self, data: dict) -> None:
        with open(self.storage_path, "w", encoding = "utf-8") as f:
            json.dump(data, f, ensure_ascii = False, indent = 4)