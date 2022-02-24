from unittest.mock import MagicMock

from telegram import Update
from telegram.ext import CallbackContext

from pomodram import main


def test_new_task__new_task__task_added():
    # given
    main.users_task_data = {1: []}

    # when
    update = MagicMock(Update)
    update.effective_chat.id = 1
    context = MagicMock(CallbackContext)
    context.args = ['Моя', 'новая', 'задача']
    main.new_task(update, context)

    # then
    assert main.users_task_data == {1: ['Моя новая задача']}
    context.bot.send_message.assert_called_once_with(1, text="Ok")