import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import telegram.ext
from telegram.ext import Updater
from selenium.webdriver.common.action_chains import ActionChains

class Main:
    def __init__(self, theme="chiikawa"):
        Chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(executable_path=".\chromedriver.exe")
        self.actions = ActionChains(self.driver)

        if theme == "chiikawa":
            self.url = f"https://chiikawamarket.jp"
        elif theme == "nagano":
            self.url = f"https://nagano-market.jp"
        self.driver.set_window_size(1024, 800)
        self.driver.get(self.url)


        input("wait for Worldship Close")
        login = self.driver.find_element(By.CSS_SELECTOR, '[alt="ログイン"]')
        login.click()
        time.sleep(1)

        email = self.driver.find_element(By.CSS_SELECTOR, '[type="email"]')
        password = self.driver.find_element(By.CSS_SELECTOR, '[type="password"]')
        submit = self.driver.find_element(By.CSS_SELECTOR, '[value="ログイン"]')
        email.send_keys("")
        password.send_keys("")
        submit.click()
        self.newitems = f"{self.url}/collections/newitems"
        # self.newitems = f"{self.url}/collections/20221123"
        # self.driver.get(self.newitems)

    def loop(self, lst="123", page=1):

        for name in lst:
            page = 1
            main_retry = 1

            while True:
                self.newitems = f"{self.url}/collections/newitems?page={page}"
                # self.newitems = f"{self.url}/collections/20221209?page={page}"
                self.driver.get(self.newitems)
                # self.driver.execute_script("location.reload(true);")

                try:
                    for i in range(1, 33):
                        if f"{lst[f'{name}'][0]}" in self.driver.find_element(By.XPATH, f"//div[contains(@class, 'product--root')][{i}]/descendant::*[contains(@class, 'product_name')]").text and \
                        f"{lst[f'{name}'][1]}" in self.driver.find_element(By.XPATH, f"//div[contains(@class, 'product--root')][{i}]/descendant::*[contains(@class, 'product_name')]").text and \
                        f"{lst[f'{name}'][2]}" in self.driver.find_element(By.XPATH, f"//div[contains(@class, 'product--root')][{i}]/descendant::*[contains(@class, 'product_name')]").text:
                            print("a", i)
                            self.driver.find_element(By.XPATH, f"//div[contains(@class, 'product--root')][{i}]/descendant::*[contains(@class, 'product_name')]").click()
                            break
                        else:
                            print("搵緊", i)

                except Exception as e:
                    # print(e)
                    # self.driver.refresh()
                    self.driver.execute_script("location.reload(true);")
                    time.sleep(0.5)
                    # print("888")

                if main_retry >= 10:
                    main_retry = 0
                    break

                if "products" in self.driver.current_url:

                    products_retry = 1

                    while True:
                        cart = self.driver.find_element(By.CSS_SELECTOR, '[class="product-form--text"]')

                        if "カートに入れる" in cart.text:
                            print("入咗車")
                            cart.click()
                            ans = 0
                            break
                        else:
                            if products_retry >= 3:
                                ans = input("retry? (Y/N)")
                                if ans == "N":
                                    break
                                elif ans == "Y":
                                    products_retry = 1
                            products_retry += 1
                            self.driver.refresh()
                            time.sleep(0.5)
                            print("未買得要refresh")

                    if ans == "N":
                        ans = 0
                        break

                if "cart" in self.driver.current_url:
                    break

                # except Exception as e:
                #     print(e)
                #     self.driver.refresh()
                #     time.sleep(0.5)
                #     print("888")

                print("未有要refresh")

                try:
                    if self.driver.find_element(By.CSS_SELECTOR, '[class="pagination--number"]'):
                        if page == 2:
                            page = 1
                        else:
                            page = 2
                            main_retry += 1

                except Exception:
                    main_retry += 1


        input("diuuuuuuuuuuuuuuuuuuuuuu")

        self.driver.get(f"{self.url}/cart")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, '[class="termsCheck"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[value="レジに進む"]').click()

        ###### payment ########
        input("123")

        self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), \"宅配便\")]")))
        self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

        ##### 支払い
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(@data-card-field-placeholder, 'カード番号')]")))

        # driver.switch_to.frame("card-fields-iframe")
        self.driver.find_element(By.XPATH, "//*[contains(@data-card-field-placeholder, 'カード番号')]").click()
        self.actions.send_keys('11')
        self.actions.perform()

        self.driver.find_element(By.XPATH, "//*[contains(@data-card-field-placeholder, 'カード所有者の名前')]").click()
        self.actions.send_keys('11')
        self.actions.perform()

        self.driver.find_element(By.XPATH, "//*[contains(@data-card-field-placeholder, '有効期限 (月/年)')]").click()
        self.actions.send_keys('11')
        self.actions.perform()

        self.driver.find_element(By.XPATH, "//*[contains(@data-card-field-placeholder, 'セキュリティコード')]").click()
        self.actions.send_keys('11')
        self.actions.perform()
        print("等你俾錢")

        # driver.find_element(By.CSS_SELECTOR, '[class="input-checkbox"]').click()
        # driver.find_element(By.CSS_SELECTOR, '[class="step__footer__continue-btn btn"]')
        time.sleep(1000)

if __name__ == "__main__":
    # lst={
    #     "a": ["サンタさん", "持ちますマスコット", "ちいかわ"],
    #     "b": ["サンタさん", "持ちますマスコット", "ハチワレ"],
    #     "c": ["サンタさん", "持ちますマスコット", "うさぎ"],
    #     "d": ["ねむい", "見守る", "ちいかわ"],
    #     "e": ["ねむい", "見守る", "ハチワレ"],
    #     "f": ["ねむい", "見守る", "うさぎ"],
    #     "g": ["サンタさん", "ぬいぐるみS", "ハチワレ"],
    #     "h": ["サンタさん", "ぬいぐるみS", "うさぎ"]
    # }

    lst = {
        "a": ["ちいかわ飯店", "サーモボトル", ""],
        "b": ["ダイレクトステンレスボトル", "レディース", ""],
        "c": ["デコステッカー2", "ガムつき", ""],
        # "d": ["トレーディング", "もっとたのしいなかま編", ""],
        # "e": ["ちいかわ", "リップ", "チーク"],
    }

    # Main().loop(lst=["ちいかわ×サンリオキャラクターズ WリングノートB6（ピンク）", "ちいかわ 汁椀茶碗セット（ちいかわ）"])
    Main().loop(lst=lst)
