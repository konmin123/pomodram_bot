from abc import ABC, abstractmethod


class UserChat(ABC):
    @abstractmethod
    def send_message(self, chat_id: int, message: str) -> None:
        ...
