from typing import Union

from pomodram.domain.timer import Timer
from pomodram.domain.user_chat import UserChat


class PomodramService:
    def __init__(self, user_chat: UserChat, timer: Timer):
        self.__users_task_data: dict[Union[int, str], list[str]] = {}
        self.__user_chat = user_chat
        self.__timer = timer

    def __init_user(self, user_id: int) -> None:
        if user_id not in self.__users_task_data:
            self.__users_task_data[user_id] = []

    def new_task(self, user_id: int, task_name: str) -> str:
        self.__init_user(user_id)

        if task_name:
            self.__users_task_data[user_id].append(task_name)
            return "ok"
        else:
            return "Введите название задачи"

    def format_list_task(self, user_id: int) -> str:
        self.__init_user(user_id)
        task_text = '\n'.join([f"{index + 1}. {value}" for index, value in enumerate(self.__users_task_data[user_id])])
        if not task_text:
            return "Нет задач. Создайте хотя бы одну задачу"
        return task_text

    def tasks(self, user_id: int) -> list[str]:
        self.__init_user(user_id)
        return self.__users_task_data[user_id]

    def del_task(self, user_id: int, task_index: int) -> str:
        self.__init_user(user_id)
        if not self.__users_task_data[user_id]:
            return "У вас нет задач для удаления"

        task_index -= 1
        max_task_index = len(self.__users_task_data[user_id])
        if task_index >= max_task_index or task_index < 0:
            return f"Индекс задачи не находится в допустимом диапазоне [1:{max_task_index}]"

        del self.__users_task_data[user_id][task_index]
        return "Задача удалена"

    def _finish_pomodoro(self, user_id: int) -> None:
        ...

    def start_work(self, user_id: int) -> None:
        self.__user_chat.send_message(user_id, 'Все задачи выполнены. Нечего начинать.')
        self.__timer.schedule(self._finish_pomodoro, 25, [user_id])

