from abc import ABC, abstractmethod

from back_end.domain.user.entity.user import User


class UserRepository(ABC):

    def __init__(self, storage_path: str):
        self.storage_path = storage_path

    @abstractmethod
    def save(self, user: User) -> User:
        """
        조립이 된 User엔티티를 받아서 DB에 집어 넣고
        User 엔티티를 반환한다.
        """
        pass

    @abstractmethod
    def find_by_id(self, user_id: str) -> User | None:
        pass

    @abstractmethod
    def delete(self, user_id: str) -> bool:     # 존재 여부를 확인
        pass