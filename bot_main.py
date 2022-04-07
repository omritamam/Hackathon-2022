APK = '5235332220:AAGyi_ydNsbTm71TVvVF5IH03vjP19TOCOQ'

import bot_const as keys
from telegram.ext import *
import bot_responses as R
import telebot

bot = telebot.TeleBot(APK)

print('bot started...')


def start_command(update, context):
    update.message.reply_text('Type something random to getttttt started')


def help_command(update, context):
    update.message.reply_text('bla bla')


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.BOT_APK, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("elli", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


@bot.message_handler(content_types=['document'])
def file_sent(message):
    bot.send_message(message.chat.id, bot.get_file_url(message.document.file_id))


main()

