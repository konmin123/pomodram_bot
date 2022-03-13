import pytest

from pomodram.domain.pomodram_service import PomodramService


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
