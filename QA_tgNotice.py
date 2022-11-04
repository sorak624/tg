import schedule
import telegram.ext
from telegram.ext import Updater
import random
import time
import telegram_send

with open('token1.txt', 'r') as f:
    TOKEN = f.read()

bot = telegram.Bot(token=TOKEN)

def timeslot():
    link = 'link: https://docs.google.com/spreadsheets/d/1TIoxUl8UIz1XOgcYqPTAVsnaTL2l2BDlLUOmbXcAtF8/edit?pli=1#gid=1152468642'
    bot = telegram.Bot(token=TOKEN)
    bot.send_message('-632566886', text='Remember to fill in timeslot 😘')
    bot.send_message('-632566886', text=link)

def water():
    bot.send_message('-632566886', text='@QASamlee @vgtkenng, 你今日換左水未呀')

def tracy():
    bot.send_message('-632566886', text='https://www.youtube.com/watch?v=L3g917ffhj8')


schedule.every().monday.at("16:00").do(water)
schedule.every().tuesday.at("16:00").do(water)
schedule.every().wednesday.at("16:00").do(water)
schedule.every().thursday.at("16:00").do(water)
schedule.every().friday.at("16:00").do(water)

schedule.every().monday.at("17:30").do(timeslot)
schedule.every().tuesday.at("17:30").do(timeslot)
schedule.every().wednesday.at("17:30").do(timeslot)
schedule.every().thursday.at("17:30").do(timeslot)
schedule.every().friday.at("17:30").do(timeslot)

# def text():
#     bot = telegram.Bot(token=TOKEN)
#     bot.send_message('-632566886', text='@_@')
#
# text()

while True:
    schedule.run_pending()
    time.sleep(1)

# tracy()

