from abc import abstractmethod

from back_end.domain.user.entity.user import User


class UserInterface:

    @abstractmethod
    def save(self) -> User:
        pass