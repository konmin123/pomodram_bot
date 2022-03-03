from telegram import Update
from telegram.ext import CallbackContext

from pomodram.domain.pomodram_service import PomodramService

pomodram_service = PomodramService()


def command(func):
    def wrapper(update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        try:
            func(update, context, chat_id)
        except Exception as e:
            print(f"ERROR: {e}")
            context.bot.send_message(chat_id, text="Oops")
    return wrapper


@command
def start(update: Update, context: CallbackContext, chat_id: int) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


@command
def new_task(update: Update, context: CallbackContext, chat_id: int) -> None:
    user_message = " ".join(context.args)
    chat_text = pomodram_service.new_task(chat_id, user_message)
    context.bot.send_message(chat_id, text=chat_text)


@command
def list_task(update: Update, context: CallbackContext, chat_id: int) -> None:
    chat_text = pomodram_service.list_task(chat_id)
    context.bot.send_message(chat_id, text=chat_text)


@command
def del_task(update: Update, context: CallbackContext, chat_id: int) -> None:
    try:
        task_index = int(context.args[0]) - 1
    except ValueError:
        context.bot.send_message(chat_id, text="Значением индекса должно быть число")
        return
    chat_text = pomodram_service.del_task(chat_id, task_index)
    context.bot.send_message(chat_id, text=chat_text)
