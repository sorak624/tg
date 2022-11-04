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
bot = telegram.Bot(token=TOKEN)
list = ['101', '姐姐', '串燒', '光榮', '小魚', '嘉寶', '0192731904608563564028409147109147']

def eat():
    food = random.choice(list)
    # bot = telegram.Bot(token=TOKEN)
    bot.send_message('-1001757236183', text='Today eat what ho?')
    time.sleep(1)
    bot.send_message('-1001757236183', text=food)
    time.sleep(1)
    bot.send_message('-1001757236183', text='Click /here redraw')
    list.remove(food)

def test():
    bot.send_message('-1001757236183', text='book chiikawawawawawawaw!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

schedule.every().monday.at("11:59").do(eat)
schedule.every().tuesday.at("11:59").do(eat)
schedule.every().wednesday.at("11:59").do(eat)
schedule.every().thursday.at("11:59").do(eat)
schedule.every().friday.at("11:59").do(eat)

schedule.every().friday.at("16:45").do(test)


while True:
    schedule.run_pending()
    time.sleep(1)


