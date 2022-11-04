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

class Main:
    def __init__(self, haveId=False, item=4907953221833, name="フェイスタオル2P", name2="123123123213213", theme = None):
        with open('token.txt', 'r') as f:
            TOKEN = f.read()
        updater = Updater(token=TOKEN)
        dispatcher = updater.dispatcher
        bot = telegram.Bot(token=TOKEN)

        Chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(executable_path=".\chromedriver.exe")
        actions = ActionChains(driver)
        # driver = webdriver.Chrome()

        self.item = 4907953221833
        # item = 4582662913660
        url = f"https://chiikawamarket.jp/collections/newitems/products/{item}"
        if theme == "nagano":
            url = f"https://nagano-market.jp/collections/newitems/products/{item}"
        driver.set_window_size(1024 , 800)
        driver.get(url)


        input("wait for Worldship Close")
        login = driver.find_element(By.CSS_SELECTOR, '[alt="ログイン"]')
        login.click()
        time.sleep(1)

        email = driver.find_element(By.CSS_SELECTOR, '[type="email"]')
        password = driver.find_element(By.CSS_SELECTOR, '[type="password"]')
        submit = driver.find_element(By.CSS_SELECTOR, '[value="ログイン"]')
        email.send_keys("sora624@hotmail.com.hk")
        password.send_keys("Fca830a1")
        submit.click()


        driver.get(url)
        # cart = driver.find_element(By.CSS_SELECTOR, '[class="product-form--text"]')


        ###### if no id - loop ######
        if haveId == False:
            if theme == None:
                driver.get("https://chiikawamarket.jp/")
            elif theme == "nagano":
                driver.get("https://nagano-market.jp/")
            while True:
                try:
                    for i in range(12):
                        # if "フェイスタオル2P BL（アイス）" in driver.find_element(By.XPATH, "//div[contains(@class, 'item_box')]/h3/a").text:
                        # if f"{name}" in driver.find_element(By.XPATH, f"//div[contains(@class, 'item_box')][{i+1}]/h3/a").text:
                        if f"{name}" in driver.find_element(By.XPATH, f"//div[contains(@class, 'item_box')][{i + 1}]/h3/a").text or f"{name2}" in driver.find_element(By.XPATH, f"//div[contains(@class, 'item_box')][{i + 1}]/h3/a").text:
                            print("a", i+1)
                            driver.find_element(By.XPATH, f"//div[contains(@class, 'item_box')][{i+1}]/h3/a").click()
                            break
                        else:
                            print("搵緊", i+1)

                    if "products" in driver.current_url:
                        print("done")
                        break
                except Exception:
                    driver.refresh()
                    time.sleep(0.5)
                    print("888")

                print("未有要refresh")
                driver.refresh()
                time.sleep(0.5)

        ###### loop ######
        if haveId == True:
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
        input("123")

        driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), \"宅配便\")]")))
        driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

        ##### 支払い
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(@data-card-field-placeholder, 'カード番号')]")))

        # driver.switch_to.frame("card-fields-iframe")
        driver.find_element(By.XPATH, "//*[contains(@data-card-field-placeholder, 'カード番号')]").click()
        actions.send_keys('11')
        actions.perform()

        driver.find_element(By.XPATH, "//*[contains(@data-card-field-placeholder, 'カード所有者の名前')]").click()
        actions.send_keys('11')
        actions.perform()

        driver.find_element(By.XPATH, "//*[contains(@data-card-field-placeholder, '有効期限 (月/年)')]").click()
        actions.send_keys('11')
        actions.perform()

        driver.find_element(By.XPATH, "//*[contains(@data-card-field-placeholder, 'セキュリティコード')]").click()
        actions.send_keys('11')
        actions.perform()
        print("等你俾錢")

        # driver.find_element(By.CSS_SELECTOR, '[class="input-checkbox"]').click()
        # driver.find_element(By.CSS_SELECTOR, '[class="step__footer__continue-btn btn"]')
        time.sleep(1000)

if __name__ == "__main__":
    # Main(haveId=True, item = 4582662913660)
    Main(haveId=False, name="2023", name2="ハッピー", theme="nagano") #nagano
    # Main(haveId=True,item=4573256428677, name="マグネット", name2="ハッピー") #chiikawa
    # Main(haveId=False, name="卯年", name2="マグネット")