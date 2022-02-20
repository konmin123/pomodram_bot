import os
from typing import Union

from telegram.ext import Updater
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler


access_token = os.getenv('ACCESS_TOKEN')

users_task_data: dict[Union[int, str], list[str]] = {}
NEW_TASK_COMMAND_NAME = 'new_task'
LIST_TASK_COMMAND_NAME = 'list_task'


def init_user(chat_id):
    if chat_id not in users_task_data:
        users_task_data[chat_id] = []


def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    try:
        init_user(chat_id)
        context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id, text="Oops")


def new_task(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    try:
        user_message = update.message.text[len(NEW_TASK_COMMAND_NAME) + 2:]
        init_user(chat_id)
        if user_message:
            users_task_data[chat_id].append(user_message)
            print(users_task_data)
            context.bot.send_message(chat_id, text="Ok")
        else:
            print(users_task_data)
            context.bot.send_message(chat_id, text="Введите название задачи")
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id, text="Oops")


def list_task(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    try:
        init_user(chat_id)
        print(users_task_data)
        task_text = '\n'.join([f"{index + 1}. {value}" for index, value in enumerate(users_task_data[chat_id])])
        if not task_text:
            task_text = "Нет задач. Создайте хотя бы одну задачу"
        context.bot.send_message(chat_id, text=task_text)
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id, text="Oops")


if __name__ == "__main__":
    updater = Updater(token=access_token, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    new_task_handler = CommandHandler(NEW_TASK_COMMAND_NAME, new_task)
    dispatcher.add_handler(new_task_handler)

    list_task_handler = CommandHandler(LIST_TASK_COMMAND_NAME, list_task)
    dispatcher.add_handler(list_task_handler)

    updater.start_polling()