import msilib.schema
import requests
import time
# from seleniumwire import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import telegram.ext
from telegram.ext import Updater
from selenium.webdriver.common.action_chains import ActionChains

with open('token.txt', 'r') as f:
    TOKEN = f.read()
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher
bot = telegram.Bot(token=TOKEN)

Chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=".\chromedriver.exe")
actions = ActionChains(driver)
# driver = webdriver.Chrome()

item = 4907953221833
# item = 4582662913660
url = f"https://chiikawamarket.jp/collections/newitems/products/{item}"
driver.set_window_size(1024 , 800)
driver.get(url)


input("wait for Worldship Close")
login = driver.find_element(By.CSS_SELECTOR, '[alt="ログイン"]')
login.click()
time.sleep(1)

email = driver.find_element(By.CSS_SELECTOR, '[type="email"]')
password = driver.find_element(By.CSS_SELECTOR, '[type="password"]')
submit = driver.find_element(By.CSS_SELECTOR, '[value="ログイン"]')
email.send_keys("sorathai624@gmail.com")
password.send_keys("test1234")
submit.click()


driver.get(url)
# cart = driver.find_element(By.CSS_SELECTOR, '[class="product-form--text"]')


###### if no id - loop ######
# driver.get("https://chiikawamarket.jp/")
# while True:
#     try:
#         for i in range(12):
#             # if "フェイスタオル2P BL（アイス）" in driver.find_element(By.XPATH, "//div[contains(@class, 'item_box')]/h3/a").text:
#             if "123123" in driver.find_element(By.XPATH, f"//div[contains(@class, 'item_box')][{i+1}]/h3/a").text:
#                 print("a", i+1)
#                 driver.find_element(By.XPATH, f"//div[contains(@class, 'item_box')][{i+1}]/h3/a").click()
#                 break
#             else:
#                 print("搵緊", i+1)
#
#         if "products" in driver.current_url:
#             print("done")
#             break
#     except Exception:
#         driver.refresh()
#         time.sleep(0.5)
#         print("888")
#
#     print("未有要refresh")
#     driver.refresh()
#     time.sleep(0.5)
#

###### loop ######
# input("loop start")
driver.get(url)
while True:
    cart = driver.find_element(By.CSS_SELECTOR, '[class="product-form--text"]')

    if "カートに入れる" in cart.text:
        print("入咗車")
        cart.click()
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="cart--title"]')))
        driver.find_element(By.CSS_SELECTOR, '[class="termsCheck"]').click()
        driver.find_element(By.CSS_SELECTOR, '[value="レジに進む"]').click()
        break
    else:
        driver.refresh()
        time.sleep(0.5)
        print("未買得要refresh")


###### payment ########

driver.find_element(By.CSS_SELECTOR, '[name="button"]').click()
WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="radio__label__primary"]')))
driver.find_element(By.CSS_SELECTOR, '[class="step__footer__continue-btn btn"]').click()

##### 支払い
# WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'section__title') and contains(text(), '支払い')]")))
WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="radio-wrapper content-box__row content-box__row--secondary card-fields-container card-fields-container--loaded card-fields-container--transitioned"]')))

# driver.switch_to.frame("card-fields-iframe")
driver.find_element(By.XPATH, "//*[contains(@class, 'field__input field__input--iframe-container') and contains(@data-card-field-placeholder, 'カード番号')]").click()
actions.send_keys('987654321000')
actions.perform()

driver.find_element(By.XPATH, "//*[contains(@class, 'field__input field__input--iframe-container') and contains(@data-card-field-placeholder, 'カードの名義人')]").click()
actions.send_keys('Harry Potter')
actions.perform()

driver.find_element(By.XPATH, "//*[contains(@class, 'field__input field__input--iframe-container') and contains(@data-card-field-placeholder, '有効期限 (月/年)')]").click()
actions.send_keys('0122')
actions.perform()

driver.find_element(By.XPATH, "//*[contains(@class, 'field__input field__input--iframe-container') and contains(@data-card-field-placeholder, 'セキュリティコード')]").click()
actions.send_keys('123')
actions.perform()
print("等你俾錢")

# driver.find_element(By.CSS_SELECTOR, '[class="input-checkbox"]').click()
# driver.find_element(By.CSS_SELECTOR, '[class="step__footer__continue-btn btn"]')
time.sleep(1000)