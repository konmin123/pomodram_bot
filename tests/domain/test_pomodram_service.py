from pomodram.domain.pomodram_service import PomodramService


def test_new_task__when_new_task__then_success_message():
    # given
    pomodram_service = PomodramService()

    # when
    result = pomodram_service.new_task(123, "123")

    # then
    assert result == "ok"


def test_new_task__when_empty_task__then_error_message():
    # given
    pomodram_service = PomodramService()

    # when
    result = pomodram_service.new_task(123, "")

    # then
    assert result == "Введите название задачи"

