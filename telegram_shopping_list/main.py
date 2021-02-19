from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackContext, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, KeyboardButton, ReplyKeyboardMarkup
import sqlalchemy


updater = Updater(token="1627394037:AAHuQ-rFgD3stJ3Ugb2LSfLSlSEeXQaKe9M")
dispatcher = updater.dispatcher


def run(update: Update, context: CallbackContext):
    # keyboard = [
    #     [
    #         InlineKeyboardButton("Переглянути списки покупок", callback_data="1")
    #     ],
    #     [
    #         InlineKeyboardButton("Створити список покупок", callback_data="2"),
    #         InlineKeyboardButton("Видалити спи", callback_data="3")
    #     ]
    # ]
    # reply_markup = InlineKeyboardMarkup(keyboard)
    keyboard = [
        [
            KeyboardButton("Переглянути всі списки"),
            KeyboardButton("Видалити список")
        ]
    ]
    reply_keyboard_markup = ReplyKeyboardMarkup(keyboard=keyboard)
    update.message.reply_text("Вітаю! Це Ваші списки покупок в Telegram.", reply_markup=reply_keyboard_markup)
    print(context)


def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"Sel opt: {query.data}")



def echo(update: Update, context: CallbackContext):
    print(update)
    list_list = ["1", 2, 390]
    keyboard = [
        [
            KeyboardButton("Створити список"),
            KeyboardButton("Видалити список")
        ],
        [
            KeyboardButton("Редагувати список")
        ]
    ]
    reply_keyboard_markup = ReplyKeyboardMarkup(keyboard=keyboard)
    update.message.reply_text("Задайте імя", reply_markup=reply_keyboard_markup)



dispatcher.add_handler(CommandHandler("run", run))
dispatcher.add_handler(CallbackQueryHandler(button))

text_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(text_handler)

updater.start_polling()
updater.idle()
