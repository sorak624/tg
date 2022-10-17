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
# item = 4549660863472
url = f"https://chiikawamarket.jp/collections/newitems/products/{item}"
driver.set_window_size(1024 , 800)
driver.get(url)


input("wait for Worldship Close")
# driver.find_element(By.CSS_SELECTOR, '[class="src-components-utils-___ModalHeader__close___GR17n"]').click()
login = driver.find_element(By.CSS_SELECTOR, '[alt="ログイン"]')
login.click()
time.sleep(1)

email = driver.find_element(By.CSS_SELECTOR, '[type="email"]')
password = driver.find_element(By.CSS_SELECTOR, '[type="password"]')
submit = driver.find_element(By.CSS_SELECTOR, '[value="ログイン"]')
email.send_keys("sorafung624@gmail.com")
password.send_keys("test1234")
submit.click()


driver.get(url)
cart = driver.find_element(By.CSS_SELECTOR, '[class="product-form--text"]')

###### loop
input("loop start")
while True:
    cart = driver.find_element(By.CSS_SELECTOR, '[class="product-form--text"]')

    if "カートに入れる" in cart.text:
        print("123156")
        cart.click()
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="cart--title"]')))
        driver.find_element(By.CSS_SELECTOR, '[class="termsCheck"]').click()
        driver.find_element(By.CSS_SELECTOR, '[value="レジに進む"]').click()
        break
    else:
        driver.refresh()
        time.sleep(0.5)
        print("777")


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

# driver.find_element(By.CSS_SELECTOR, '[class="input-checkbox"]').click()
# driver.find_element(By.CSS_SELECTOR, '[class="step__footer__continue-btn btn"]')
time.sleep(1000)