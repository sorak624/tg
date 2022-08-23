import random
import time
import telegram.ext
# from telegram.ext import Updater
# from telegram.ext import MessageHandler, Filters, CommandHandler, CallbackQueryHandler
# from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram import *
from telegram.ext import *
from random import randint
from requests import get

with open('token1.txt', 'r') as f:
    TOKEN = f.read()

updater = Updater(token=TOKEN)
bot = telegram.Bot(token=TOKEN)
dispatcher = updater.dispatcher

with open("./data/blacklist.txt", encoding="utf-8") as f:
    bl = f.read()

with open("./data/wifi.txt", encoding="utf-8") as f:
    wf = f.read()

with open("./data/crypto.txt", encoding="utf-8") as f:
    ct = f.read()

with open("./data/cgp.txt", encoding="utf-8") as f:
    cgp = f.read()


def start(update, context):
    update.message.reply_text('What do you want arr?',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton('Blacklist', callback_data = '1'),
            InlineKeyboardButton('Wifi', callback_data = '2'),
            InlineKeyboardButton('Crypto path', callback_data='3')],
            [InlineKeyboardButton('Animation Panel', url = 'http://18.163.158.97:81/inplay/football'),
            InlineKeyboardButton('Testlink', url = 'http://192.168.21.53:81/testlink/index.php'),
            InlineKeyboardButton('FlyVPN', callback_data = '6')],
            [InlineKeyboardButton('CGP & GAO PAO', callback_data = '4'),
            InlineKeyboardButton('App Req. Spec', url = 'https://docs.google.com/presentation/d/1_j2fdOh6a_GzFrYxOQrMwFpCCF0bGMMSxjKfZ0uTFOw/edit#slide=id.g137eb4812c8_1_9'),
            InlineKeyboardButton('Jenkins CDAV4 account', callback_data = '5')],
            [InlineKeyboardButton('Phone rule', callback_data = '7'), InlineKeyboardButton('Zeplin', callback_data = '8')]
        ]))


def answer(update, context):
    query = update.callback_query.data

    if '1' in query:
        update.callback_query.edit_message_text(bl)
    elif '2' in query:
        update.callback_query.edit_message_text(wf)
    elif '3' in query:
        update.callback_query.edit_message_text(ct)
    elif '4' in query:
        update.callback_query.edit_message_text(cgp)
    elif '5' in query:
        update.callback_query.edit_message_text('qa\n2Eu*_/P97>d+y29[')
    elif '6' in query:
        update.callback_query.edit_message_text('slouiselen@gmail.com\n5wDBmvyeXfgb6t2')
    elif '7' in query:
        update.callback_query.edit_message_text('Validation rules\nHong Kong:\n+852: ^[4,5,6,7,8,9]{1}[0-9]{7}$\nMacau:\n+853: ^[6]{1}[0-9]{7}$\nChina:\n+86: ^[1]{1}[0-9]{10}$\nMalaysia:\n+60: ^(0)?1[0-9]{1}[0-9]{7,8}$\nSingapore:\n+65: ^[6,8,9]{1}[0-9]{7}$\nPhilippines:\n+63: ^(0)?9[0-9]{9}$\nIndonesia:\n+62: ^[0-9]{10,13}\nVietnam:\n+84: ^[0]{1}[0-9]{10}')
    elif '8' in query:
        update.callback_query.edit_message_text('vgtqa@vgt-hk.net \n vgtqa2019')

# def messageHandler(update, context: CallbackContext):
#     image = get("https://img.discuss.com.hk/d/attachments/day_220210/20220210_705caf40509687c88fb3C7nbz8CUqoLl.jpg").content
#     for a in sam:
#         if a == update.message.text:
#             context.bot.send_message(chat_id = update.effective_chat.id, text = "{} is GAY".format(update.message.text))
#
#     if "Anson lo" in update.message.text:
#         context.bot.sendMediaGroup(chat_id = update.effective_chat.id, media = [InputMediaPhoto(image, caption="")])
#
#         buttons = [[InlineKeyboardButton("ðŸ‘�ðŸ�»", callback_data="like")], [InlineKeyboardButton("ðŸ‘ŽðŸ�»", callback_data="dislike")]]
#         context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text="Did you like this image?")


dispatcher.add_handler(CommandHandler('start', start))
# dispatcher.add_handler(CommandHandler('test', test))
# dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))
dispatcher.add_handler(CallbackQueryHandler(answer))

updater.start_polling()
updater.idle()