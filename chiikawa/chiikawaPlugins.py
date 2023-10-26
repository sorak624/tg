import time
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


date = "20230901"

with open('goods.json', encoding='utf-8') as file:
    data = json.load(file)
goods = data['items']
print(f"goods:{goods}")
homepage = "https://chiikawamarket.jp"

def chii_Main(driver, url):
    try:
        window_handles_count = len(driver.window_handles)
        if window_handles_count > 1:
            driver.switch_to.window(driver.window_handles[0])
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

    except Exception as excSwithFail:
        pass
    if '/cart' in url:
        chii_payment(driver)

    if f'/collections/{date}' in url:
        purchase_all_items(driver, goods)

    try:
        if driver.find_element(By.CSS_SELECTOR, 'img[alt="ログイン"]'):
            driver.find_element(By.CSS_SELECTOR, 'img[alt="ログイン"').click()
            chii_login(driver, url)

    except Exception as e:
        print("find next button fail")
        print(e)
        pass


def chii_login(driver, url, date=date):
    try:
        if '/login' in url:

            email = driver.find_element(By.CSS_SELECTOR, 'input.text[type="email"]')
            password = driver.find_element(By.CSS_SELECTOR, 'input.text[type="password"]')
            submit = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"][value="ログイン"]')
            email.send_keys("sorafung624@gmail.com")
            password.send_keys("Fca830a1")
            submit.click()
            time.sleep(2)
            driver.refresh()

            if '/account' in url:
                driver.find_element(By.XPATH, '//h3[text()="会員登録情報"]')
                driver.get(f"{homepage}/collections/{date}")

    except Exception as e:
        print("find next button fail")
        pass

def search_item(driver, good):
    n = 0
    while n <= 3:
        try:
            search_box = driver.find_element(By.CSS_SELECTOR, 'div.sub input[type="search"]')
            search_submit = driver.find_element(By.CSS_SELECTOR, 'div.sub button[type="submit"]')

            search_box.clear()
            search_box.send_keys(good)
            search_submit.click()

            try:
                if not driver.find_element(By.XPATH, "//div[contains(text(),'0 results')]"):
                    break
                else:
                    driver.execute_script("location.reload(true);")
                    time.sleep(0.5)
                    n += 1
            except NoSuchElementException:
                break
        except Exception as e:
            print(e)




def purchase_all_items(driver, goods):
    input("wait for start")
    for good in goods:
        print(good)
        search_item(driver, good)

        chii_loop(driver, good)

    chii_payment()

def chii_loop(driver, good):

    try:
        for i in range(1, 33):
            if driver.find_element(By.XPATH, f"//div[contains(text(), '{good}')]"):

                productName = driver.find_element(By.XPATH,
                                                  f"//div[contains(@class, 'product--root')][{i}]/descendant::*[contains(@class, 'product_name')]")
                name = productName.text
                productName.click()
                chii_purchase(driver, name)
                break

    except Exception as e:
        driver.execute_script("location.reload(true);")
        time.sleep(0.5)



def chii_purchase(driver, name):
    ret = False
    if "/products" in driver.current_url:

        try:
            if driver.find_element(By.CSS_SELECTOR, '[value="同意します"]'):
                time.sleep(1)
                driver.find_element(By.CSS_SELECTOR, '[value="同意します"]').click()
        except Exception:
            print("No tick box")

        cart = driver.find_element(By.CSS_SELECTOR, '[class="product-form--text"]')

        if "カートに入れる" in cart.text:
            print(f"{name} 入咗車")
            cart.click()
            ret = True
        else:
            ret = "sold out"

    return ret


def chii_payment(driver):
    actions = ActionChains(driver)
    try:
        if "/cart" in driver.current_url:
            driver.find_element(By.CSS_SELECTOR, '[class="termsCheck"]').click()
            input("ok mei?????????????????????????????????????????")
            driver.find_element(By.CSS_SELECTOR, 'button[name="checkout"]').click()

            ###### payment ########
            print("step")
            input("quening")

            driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
            WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), \"宅配便\")]")))
            driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

            ##### 支払い
            print("123")
            # WebDriverWait(driver, 30).until(
            #     EC.element_to_be_clickable((By.XPATH, "//*[contains(@class, 'input-placeholder-color') and contains(@placeholder, 'カード番号')]")))
            WebDriverWait(driver, 30).until(
               EC.element_to_be_clickable((By.CSS_SELECTOR, "div.radio-wrapper.content-box__row.content-box__row--secondary.card-fields-container.card-fields-container--loaded.card-fields-container--transitioned")))

            # driver.switch_to.frame("card-fields-iframe")
            print("3333")
            driver.find_element(By.XPATH, "//*[contains(@data-card-field-placeholder, 'カード番号')]").click()
            actions.send_keys('1111')
            actions.perform()

            driver.find_element(By.XPATH, "//*[contains(@data-card-field-placeholder, 'カードの名義人')]").click()
            actions.send_keys('2222')
            actions.perform()

            driver.find_element(By.XPATH, "//*[contains(@data-card-field-placeholder, '有効期限 (月/年)')]").click()
            actions.send_keys('4444')
            actions.perform()

            driver.find_element(By.XPATH, "//*[contains(@data-card-field-placeholder, 'セキュリティコード')]").click()
            actions.send_keys('5555')
            actions.perform()
            input("等你俾錢")
    except Exception as e:
        input(e)

        # driver.find_element(By.CSS_SELECTOR, '[class="input-checkbox"]').click()
        # driver.find_element(By.CSS_SELECTOR, '[class="step__footer__continue-btn btn"]')
