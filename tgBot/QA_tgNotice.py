import schedule
import telegram.ext
from telegram.ext import Updater
import random
import time
import telegram_send
from datetime import date
import holidays

red = holidays.HK
red = holidays.country_holidays('HK')
today = date.today()

with open('token1.txt', 'r') as f:
    TOKEN = f.read()

bot = telegram.Bot(token=TOKEN)

def timeslot():
    link = 'link: https://docs.google.com/spreadsheets/d/1TIoxUl8UIz1XOgcYqPTAVsnaTL2l2BDlLUOmbXcAtF8/edit?pli=1#gid=733474337'
    bot = telegram.Bot(token=TOKEN)
    bot.send_message('-632566886', text='Remember to fill in timeslot 😘')
    bot.send_message('-632566886', text=link)

def water():
    bot.send_message('-632566886', text='@vgtkenng, 你今日換左水未呀')

def todayTime():
    print(f'Today ({today}) is {red.get(today)}')
    bot.send_message('-1001757236183', text=f'Today ({today}) is {red.get(today)}')


if red.get(today) == None:
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

else:
    # schedule.every().day.at("11:59").do(print(f'Today{today} is {red.get(today)}'))
    schedule.every().day.at("11:59").do(todayTime)

# def text():
#     bot = telegram.Bot(token=TOKEN)
#     bot.send_message('-632566886', text='@_@')
#
# text()

while True:
    today = date.today()
    schedule.run_pending()
    time.sleep(1)

