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
from datetime import date
import holidays
import requests
import poke
import golandAC
from golandAC import *
import re

red = holidays.HK
red = holidays.country_holidays('HK')
chatId = "-827809820"

with open('token.txt', 'r') as f:
    TOKEN = f.read()

with open('app.txt', 'r') as f:
    appTxt = f.read()

inputBox = []

updater = Updater(token=TOKEN)
bot = telegram.Bot(token=TOKEN)
dispatcher = updater.dispatcher

list = ['101', '姐姐', '串燒', '光榮', '小魚', '嘉寶', '拉麵']
sam = ['sam', 'ken', 'Ken', 'Sam']


def again(update, context):
    update.message.reply_text("今日食咩好????", reply_markup = InlineKeyboardMarkup([[
            InlineKeyboardButton('re', callback_data = 'food')
            ]]))
    # list.remove(food)

def todayIs(update, context):
    today = date.today()
    update.message.reply_text(f'{red.get(today)}')
    # update.message.reply_text(f"{red.get('2023-1-2')}")

def start(update, context):
    update.message.reply_text('What do you want arr?',
        reply_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton('live', url = 'http://18.163.158.97:81/inplay/football'),
            InlineKeyboardButton('Testlink', url = 'http://192.168.21.53:81/testlink/index.php'),
            InlineKeyboardButton('APP dev', url='http://192.168.17.77:88/d20/')],
            [InlineKeyboardButton('figma', url = 'https://www.figma.com/file/4dgOlg3ihsSEbXTIWAigO0/APP-V3-Sport---DEMO-(6)-2022-06-09?node-id=11893%3A63030'),
            InlineKeyboardButton('App Download　URL', url = 'https://web01.app-store-update.com/v2android/mobileV3/download_mobilev3.html'),
            InlineKeyboardButton('App build bundle', callback_data = '6')],
            [InlineKeyboardButton('Jenkins CDAV4', callback_data = '5'),InlineKeyboardButton('Phone rule', callback_data = '7')],
            [InlineKeyboardButton('Zeplin', callback_data = '8')]
        ]))


def answer(update, context):
    query = update.callback_query.data

    if 'food' in query:
        food = random.choice(list)
        n = random.randint(1, 7)
        n = str(n)
        update.callback_query.edit_message_text(food + "      " + n, reply_markup = InlineKeyboardMarkup([[
            InlineKeyboardButton('re', callback_data = 'food')
            ]]))
    elif 'like' in query:
        update.callback_query.edit_message_text('https://www.youtube.com/watch?v=H5ivE_QZTcw')
    elif '5' in query:
        update.callback_query.edit_message_text('qa   2Eu*_/P97>d+y29[')
    elif '6' in query:
        update.callback_query.edit_message_text(appTxt)
    elif '7' in query:
        update.callback_query.edit_message_text('Validation rules\nHong Kong:\n+852: ^[4,5,6,7,8,9]{1}[0-9]{7}$\nMacau:\n+853: ^[6]{1}[0-9]{7}$\nChina:\n+86: ^[1]{1}[0-9]{10}$\nMalaysia:\n+60: ^(0)?1[0-9]{1}[0-9]{7,8}$\nSingapore:\n+65: ^[6,8,9]{1}[0-9]{7}$\nPhilippines:\n+63: ^(0)?9[0-9]{9}$\nIndonesia:\n+62: ^[0-9]{10,13}\nVietnam:\n+84: ^[0]{1}[0-9]{10}')
    elif '8' in query:
        update.callback_query.edit_message_text('vgtqa@vgt-hk.net \n vgtqa2019')


def golandToken(update, context):
    sentence = update.message.text[13:].replace('\n', '')
    print(sentence)
    update.message.reply_text(golandAC.golandAccount().login(username=sentence))


def messageHandler(update, context: CallbackContext):
    image = get("https://img.discuss.com.hk/d/attachments/day_220210/20220210_705caf40509687c88fb3C7nbz8CUqoLl.jpg").content
    for a in sam:
        if a == update.message.text:
            context.bot.send_message(chat_id = update.effective_chat.id, text = "{} is GAY".format(update.message.text))

    # if "Anson lo" in update.message.text:
    #     context.bot.sendMediaGroup(chat_id = update.effective_chat.id, media = [InputMediaPhoto(image, caption="")])
    #
    #     buttons = [[InlineKeyboardButton("ðŸ‘�ðŸ�»", callback_data="like")], [InlineKeyboardButton("ðŸ‘ŽðŸ�»", callback_data="dislike")]]
    #     context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text="Did you like this image?")

def help(update, context):
    update.message.reply_text("/help -- command list\n/start -- general function\n/golandToken {username} -- generate websocket access token")

def pokeHelp(update, context):
    update.message.reply_text(
        "Please input /def1 \"type\" -- 一般", "火", "水", "電", "草", "冰", "格鬥", "毒", "地面", "飛行", "超能力", "蟲", "岩石", "幽靈", "龍", "惡", "鋼", "妖精")

def messageHandler(update, context: CallbackContext):

    if "/def" in update.message.text:
        try:
            matchObj = re.match(r'/def (.*) (.*)', update.message.text)
            type1 = matchObj.group(1)
            type2 = matchObj.group(2)

        except:
            matchObj = re.match(r'/def (.*)', update.message.text)
            type1 = matchObj.group(1)
            type2 = None

        Poke = poke.poke()
        a = Poke.result(def1=type1, def2=type2)
        # update.message.reply_text(text=a)
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'{a}'.format(update.message.text))



dispatcher.add_handler(CommandHandler('here', again))
dispatcher.add_handler(CommandHandler('today', todayIs))
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('pokeHelp', pokeHelp))
dispatcher.add_handler(CommandHandler('golandToken', golandToken))
dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))
dispatcher.add_handler(CallbackQueryHandler(answer))

updater.start_polling()
updater.idle()