import os

from telegram.ext import Updater
from telegram.ext import CommandHandler

from pomodram.api.handlers import start, new_task, list_task, del_task

access_token = os.getenv('ACCESS_TOKEN')

NEW_TASK_COMMAND_NAME = 'new_task'
LIST_TASK_COMMAND_NAME = 'list_task'
DEL_TASK_COMMAND_NAME = 'del_task'


if __name__ == "__main__":
    updater = Updater(token=access_token, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    new_task_handler = CommandHandler(NEW_TASK_COMMAND_NAME, new_task)
    dispatcher.add_handler(new_task_handler)

    list_task_handler = CommandHandler(LIST_TASK_COMMAND_NAME, list_task)
    dispatcher.add_handler(list_task_handler)

    del_task_handler = CommandHandler(DEL_TASK_COMMAND_NAME, del_task)
    dispatcher.add_handler(del_task_handler)

    updater.start_polling()
