from typing import Union


class PomodramService:
    def __init__(self):
        self.__users_task_data: dict[Union[int, str], list[str]] = {}

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

    def list_task(self, user_id: int) -> str:
        self.__init_user(user_id)
        task_text = '\n'.join([f"{index + 1}. {value}" for index, value in enumerate(self.__users_task_data[user_id])])
        if not task_text:
            return "Нет задач. Создайте хотя бы одну задачу"
        return task_text

    def del_task(self, user_id: int, task_index: int) -> str:
        self.__init_user(user_id)
        if not self.__users_task_data[user_id]:
            return "У вас нет задач для удаления"

        max_task_index = len(self.__users_task_data[user_id])
        if task_index >= max_task_index or task_index < 0:
            return f"Индекс задачи не находится в допустимом диапазоне [1:{max_task_index}]"

        del self.__users_task_data[user_id][task_index]
        return "Задача удалена"
