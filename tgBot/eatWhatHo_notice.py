import schedule
import telegram.ext
from telegram.ext import Updater
import random
import time
import requests
from datetime import date
from datetime import datetime
import holidays

red = holidays.HK
red = holidays.country_holidays('HK')
today = date.today()
# today = "2023-01-02"
chatId = "-827809820"

with open('token.txt', 'r') as f:
    TOKEN = f.read()

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher
bot = telegram.Bot(token=TOKEN)
list = ['101', '姐姐', '串燒', '光榮', '小魚', '嘉寶', '0192731904608563564028409147109147']

## Hang Seng JPY tt Exchange Rate ##
url = "https://rbwm-api.hsbc.com.hk/pws-hk-hase-rates-papi-prod-proxy/v1/fxtt-exchange-rates?isIncludeCcyNameLang=N"


def eat():
    food = random.choice(list)
    # bot = telegram.Bot(token=TOKEN)
    bot.send_message(chatId, text='Today eat what ho?')
    time.sleep(1)
    bot.send_message(chatId, text=food)
    time.sleep(1)
    bot.send_message(chatId, text='Click /here redraw')
    list.remove(food)

def test():
    bot.send_message(chatId, text=current_time)

def todayTime():
    print(f'Today ({today}) is {red.get(today)}')
    bot.send_message(chatId, text=f'Today ({today}) is {red.get(today)}')

def jpRate():
    session_requests = requests.session()
    exchange = session_requests.request("GET", url, headers={})
    exchange = exchange.json()

    for n in exchange['fxttExchangeRates']:
        if n['ccyCode'] == 'JPY':
            if int(float(n['ttSellRate'])) > 58:
                print(n['ccyCode'], "is", n['ttSellRate'], 'now')
                bot.send_message(chatId, text=f"dllm {n['ccyCode']} is {n['ttSellRate']} now")
            elif int(float(n['ttSellRate'])) < 57:
                print(n['ccyCode'], "is", n['ttSellRate'], 'now')
                bot.send_message(chatId, text=f"!!!!!!!!!!!!!! {n['ccyCode']} is {n['ttSellRate']} now")

# schedule.every(0.1).minutes.do(test)

if red.get(today) == None:
    schedule.every().monday.at("11:59").do(eat)
    schedule.every().tuesday.at("11:59").do(eat)
    schedule.every().wednesday.at("11:59").do(eat)
    schedule.every().thursday.at("11:59").do(eat)
    schedule.every().friday.at("11:59").do(eat)
    # schedule.every(0.1).minutes.do(jpRate)

else:
    # schedule.every().day.at("11:59").do(print(f'Today{today} is {red.get(today)}'))
    schedule.every().day.at("11:59").do(todayTime)


while True:
    today = date.today()
    schedule.run_pending()
    time.sleep(1)


