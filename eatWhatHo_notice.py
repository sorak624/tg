import schedule
import telegram.ext
from telegram.ext import Updater
import random
import time
import telegram_send


with open('token.txt', 'r') as f:
    TOKEN = f.read()

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

list = ['å§�å§�', 'ä¸²ç‡’', '101', 'é­šç”Ÿ', 'å˜‰å¯¶', 'å…‰æ¦®', 'å°�é­š', 'é�µç‰›']

def eat():
    food = random.choice(list)
    bot = telegram.Bot(token=TOKEN)
    bot.send_message('-1001757236183', text='Today eat what ho?')
    time.sleep(1)
    bot.send_message('-1001757236183', text=food)
    time.sleep(1)
    bot.send_message('-1001757236183', text='Click /here redraw')
    list.remove(food)


schedule.every().monday.at("11:59").do(eat)
schedule.every().tuesday.at("11:59").do(eat)
schedule.every().wednesday.at("11:59").do(eat)
schedule.every().thursday.at("11:59").do(eat)
schedule.every().friday.at("11:59").do(eat)


while True:
    schedule.run_pending()
    time.sleep(1)


