import os
from typing import Union

from telegram.ext import Updater
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler


access_token = os.getenv('ACCESS_TOKEN')

users_task_data: dict[Union[int, str], list[str]] = {}
NEW_TASK_COMMAND_NAME = 'new_task'


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def new_task(update: Update, context: CallbackContext):
    try:
        chat_id = update.effective_chat.id
        if chat_id not in users_task_data:
            users_task_data[chat_id] = []
        users_task_data[chat_id].append(update.message.text[len(NEW_TASK_COMMAND_NAME) + 2:])
        print(users_task_data)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Ok")
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Oops")


if __name__ == "__main__":
    updater = Updater(token=access_token, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    new_task_handler = CommandHandler(NEW_TASK_COMMAND_NAME, new_task)
    dispatcher.add_handler(new_task_handler)

    updater.start_polling()
