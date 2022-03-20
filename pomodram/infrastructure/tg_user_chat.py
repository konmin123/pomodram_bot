from pomodram.domain.user_chat import UserChat


class TgUserChat(UserChat):
    def send_message(self, chat_id: int, message: str) -> None:
        raise NotImplemented
