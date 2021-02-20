from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackContext, CallbackQueryHandler, ConversationHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, KeyboardButton, ReplyKeyboardMarkup
import sqlite_query

updater = Updater(token="1627394037:AAHuQ-rFgD3stJ3Ugb2LSfLSlSEeXQaKe9M")
dispatcher = updater.dispatcher

USER_ID = 0

def run(update: Update, context: CallbackContext):
    USER_ID = update.message.from_user.id
    print(USER_ID)
    sqlite_query.add_user(USER_ID)
    keyboard = [
        [
            KeyboardButton("Переглянути всі списки"),
            KeyboardButton("Створити список покупок")
        ]
    ]
    reply_keyboard_markup = ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )
    update.message.reply_text(
        "Вітаю! Це Ваші списки покупок в Telegram.",
        reply_markup=reply_keyboard_markup
    )

def button(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "view_list":
        selector(update, context)
    if query.data == "create_list":
        query.message.reply_text("Введіть назву списку")
        text_handler = MessageHandler(Filters.text, create_new_list)
        dispatcher.add_handler(text_handler)
    if query.data == "add_good":
        query.message.reply_text("Вводбте назви продуктів")
        text_handler = MessageHandler(Filters.text, edit_list)
        dispatcher.add_handler(text_handler)

title = ""
list_id = None

def create_new_list(update: Update, context: CallbackContext):
    title = update.message.text
    sqlite_query.create_list(title, USER_ID)
    list_id = sqlite_query.get_list_id(USER_ID, title)
    if update.message.text:
        keyboard = [
            [
                InlineKeyboardButton("Додати", callback_data="add_good")
            ]
        ]
        replay_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text("Додайте продукт", reply_markup=replay_markup)
        return edit_list

    # query.message.reply_text("Вводьте назви продуктів")

def delete_list():
    pass


def edit_list(update: Update, context: CallbackContext):
    name_good = update.message.text
    sqlite_query.add_goods(name_good, title)
    all_goods = ""
    for instance in sqlite_query.view_all_goods(list_id):
        all_goods += instance
    update.message.reply_text(all_goods)

def selector(update: Update, context: CallbackContext):
    text = update.message.text
    print(f"text {text}")
    keyboard_all = [
        [
            InlineKeyboardButton("Переглянути всі списки", callback_data="view_list"),
            InlineKeyboardButton("Створити список покупок", callback_data="create_list")
        ],
        [
            InlineKeyboardButton("Редагувати список покупок", callback_data="edit_list"),
            InlineKeyboardButton("Видалити список", callback_data="delete_list")
        ]
    ]
    keyboard_part1 = [
        [
            InlineKeyboardButton("Створити список покупок", callback_data="create_list")
        ],
        [
            InlineKeyboardButton("Редагувати список покупок", callback_data="edit_list"),
            InlineKeyboardButton("Видалити список", callback_data="delete_list")
        ]
    ]
    keyboard_part2 = [
        [
            InlineKeyboardButton("Редагувати список покупок", callback_data="edit_list"),
            InlineKeyboardButton("Видалити список", callback_data="delete_list")
        ]
    ]
    reply_markup_all = InlineKeyboardMarkup(keyboard_all)
    reply_markup_part1 = InlineKeyboardMarkup(keyboard_part1)
    reply_markup_part2 = InlineKeyboardMarkup(keyboard_part2)
    if text == "Переглянути всі списки":
        print(text)
        if len(sqlite_query.view_all_lists(USER_ID)) == 0:
            update.message.reply_text(
                "У вас ще немає списків покупок. Створіть список",
                reply_markup=reply_markup_part2
            )
        else:
            for instance in sqlite_query.view_all_lists(USER_ID):
                update.message.reply_text(
                    f"{instance[1]}",
                    reply_markup=reply_markup_part2
                )
    elif text == "Створити список покупок":
        update.message.reply_text("Введіть назву списку")
        text_handler = MessageHandler(Filters.text, create_new_list)
        dispatcher.add_handler(text_handler)
    else:
        update.message.reply_text("Виберіть дію", reply_markup=reply_markup_all)


# conversation_handler = ConversationHandler(
#     entry_points=[CommandHandler("run", run)],
#     states={
#         VIEW_LIST: []
#     }
# )
dispatcher.add_handler(CommandHandler("start", run))
dispatcher.add_handler(CallbackQueryHandler(button))

text_handler_view = MessageHandler(Filters.regex("Переглянути всі списки"), selector)
text_handler_create = MessageHandler(Filters.regex("Створити список покупок"), selector)
text_handler_edit = MessageHandler(Filters.regex("Редагувати список покупок"), selector)
text_handler_delete = MessageHandler(Filters.regex("Видалити список"), selector)
dispatcher.add_handler(text_handler_view)
dispatcher.add_handler(text_handler_create)
dispatcher.add_handler(text_handler_edit)
dispatcher.add_handler(text_handler_delete)

updater.start_polling()
updater.idle()
