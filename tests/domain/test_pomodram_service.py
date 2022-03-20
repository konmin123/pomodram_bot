from unittest.mock import MagicMock, ANY

import pytest

from pomodram.domain.pomodram_service import PomodramService
from pomodram.domain.timer import Timer
from pomodram.domain.user_chat import UserChat


@pytest.mark.parametrize("task_name, expected_result", [("123", "ok"), ("", "Введите название задачи")])
def test_new_task__when_new_task__then_message(task_name: str, expected_result: str,):
    # given
    pomodram_service = PomodramService()

    # when
    result = pomodram_service.new_task(123, task_name)

    # then
    assert result == expected_result


@pytest.mark.parametrize(
    "tasks, expected_result",
    [
        ([], "Нет задач. Создайте хотя бы одну задачу"),
        (["abc", "def"], "1. abc\n2. def")
    ]
)
def test_format_list_task__when_tasks__then_correct_list(tasks: list[str], expected_result: str):
    # given
    pomodram_service = PomodramService()
    for t in tasks:
        pomodram_service.new_task(123, t)

    # when
    result = pomodram_service.format_list_task(123)

    # then
    assert result == expected_result


@pytest.mark.parametrize(
    "tasks, index, expected_tasks, expected_result",
    [
        ([], 1, [], "У вас нет задач для удаления"),
        (["123"], 2, ["123"], "Индекс задачи не находится в допустимом диапазоне [1:1]"),
        (["123"], 0, ["123"], "Индекс задачи не находится в допустимом диапазоне [1:1]"),
        (["123"], 1, [], "Задача удалена")
    ]
)
def test_del_task__when_task_index__then_correct_answer(
        tasks: list[str], index: int, expected_tasks: list[str], expected_result: str
):
    # given
    pomodram_service = PomodramService()
    for t in tasks:
        pomodram_service.new_task(123, t)

    # when
    result = pomodram_service.del_task(123, index)

    # then
    assert result == expected_result
    assert pomodram_service.tasks(123) == expected_tasks


def test_start_work__when_no_pomodoros__then_warning_message():
    # given
    user_chat = MagicMock(UserChat)
    service = PomodramService(user_chat)

    # when
    service.start_work(42)

    # then
    user_chat.send_message.assert_called_once_with(42, 'Все задачи выполнены. Нечего начинать.')


def test_start_work__when_one_pomodoro__then_plan_pomodor_and_break():
    # given
    user_chat = MagicMock(UserChat)
    timer = MagicMock(Timer)
    service = PomodramService(user_chat, timer)
    service.new_task(42, 'Task 1')

    # when
    service.start_work(42)

    # then
    timer.schedule.assert_called_with(service._finish_pomodoro, 25, [42])


def test_finish_pomodoro__when_one_pomodoro__then__finish():
    # given
    user_chat = MagicMock(UserChat)
    service = PomodramService(user_chat, MagicMock(Timer))
    service.new_task(42, 'Task 1')

    # when
    service._finish_pomodoro(42)

    # then
    user_chat.send_message.assert_called_once_with(42, 'Все задачи выполнены')
