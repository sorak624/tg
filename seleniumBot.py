import time
import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import requests

def get_app_root():
    # 讀取檔案裡的參數值
    basis = ""
    if hasattr(sys, 'frozen'):
        basis = sys.executable
    else:
        basis = sys.argv[0]
    app_root = os.path.dirname(basis)
    return app_root

def get_favoriate_extension_path(webdriver_path):
    no_google_analytics_path = os.path.join(webdriver_path,"no_google_analytics_1.1.0.0.crx")
    no_ad_path = os.path.join(webdriver_path,"Adblock_3.14.2.0.crx")
    return no_google_analytics_path, no_ad_path

def get_driver_by_config(driver_type):
    homepage = "https://ticketing.galaxymacau.com/shows/show.aspx?sh=YGTTEV"

    Root_Dir = get_app_root()
    webdriver_path = os.path.join(Root_Dir, "webdriver")
    adblock_plus_enable = True
    print("adblock_plus_enable:", adblock_plus_enable)
    if driver_type != "uc":
        driver = load_chromdriver_normal(webdriver_path, driver_type, adblock_plus_enable)
    else:
        driver = load_chromdriver_uc(webdriver_path, adblock_plus_enable)

    if driver is None:
        print("create web driver object fail @_@;")
    else:
        try:
            print("goto url:", homepage)

            if homepage == "https://tixcraft.com":
                homepage = "https://tixcraft.com/user/changeLanguage/lang/zh_tw"

            driver.get(homepage)

            # driver.switch_to.window(driver.window_handles[0])
            # # if "adblock" in driver.current_url:
            # driver.close()
            # driver.switch_to.window(driver.window_handles[0])
            # driver.get(homepage)

        except WebDriverException as exce2:
            print('oh no not again, WebDriverException')
            print('WebDriverException:', exce2)
        except Exception as exce1:
            print('get URL Exception:', exce1)
            pass

    return driver

def load_chromdriver_normal(webdriver_path, driver_type, adblock_plus_enable):
    chrome_options = webdriver.ChromeOptions()

    chromedriver_path = os.path.join(webdriver_path,"chromedriver.exe")


    # some windows cause: timed out receiving message from renderer
    if adblock_plus_enable:
        # PS: this is ocx version.
        no_google_analytics_path, no_ad_path = get_favoriate_extension_path(webdriver_path)

        if os.path.exists(no_google_analytics_path):
            print("123123213123123123")
            chrome_options.add_extension(no_google_analytics_path)
        if os.path.exists(no_ad_path):
            chrome_options.add_extension(no_ad_path)

    # proxy = 123
    # chrome_options.add_argument(f'--proxy-server={proxy}')
    chrome_options.add_argument('--disable-features=TranslateUI')
    chrome_options.add_argument('--disable-translate')
    chrome_options.add_argument('--lang=zh-TW')

    # for navigator.webdriver
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_experimental_option("prefs", {"credentials_enable_service": False, "profile.password_manager_enabled": False})

    #caps = DesiredCapabilities().CHROME
    caps = chrome_options.to_capabilities()

    #caps["pageLoadStrategy"] = u"normal"  #  complete
    caps["pageLoadStrategy"] = u"eager"  #  interactive
    #caps["pageLoadStrategy"] = u"none"

    #caps["unhandledPromptBehavior"] = u"dismiss and notify"  #  default
    #caps["unhandledPromptBehavior"] = u"ignore"
    #caps["unhandledPromptBehavior"] = u"dismiss"
    caps["unhandledPromptBehavior"] = u"accept"

    chrome_service = Service(chromedriver_path)
    # method 6: Selenium Stealth
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options, desired_capabilities=caps)

    if driver_type=="stealth":
        from selenium_stealth import stealth
        # Selenium Stealth settings
        stealth(driver,
              languages=["zh-TW", "zh"],
              vendor="Google Inc.",
              platform="Win32",
              webgl_vendor="Intel Inc.",
              renderer="Intel Iris OpenGL Engine",
              fix_hairline=True,
          )
    #print("driver capabilities", driver.capabilities)

    return driver

def load_chromdriver_uc(webdriver_path, adblock_plus_enable):
    print('Get current working directory : ', os.getcwd())
    import undetected_chromedriver as uc

    chromedriver_path = os.path.join(webdriver_path,"chromedriver.exe")
    # chromedriver_path = "c:\\Users\\qa_sora\\PycharmProjects\\tg\\webdriver\\chromedriver.exe"

    print(chromedriver_path)

    options = uc.ChromeOptions()
    options.page_load_strategy="eager"

    if adblock_plus_enable:
        no_google_analytics_path, no_ad_path = get_favoriate_extension_path(webdriver_path)
        print(get_favoriate_extension_path(webdriver_path))
        no_google_analytics_folder_path = no_google_analytics_path.replace('.crx','')
        no_ad_folder_path = no_ad_path.replace('.crx','')
        load_extension_path = ""
        if os.path.exists(no_google_analytics_folder_path):
            load_extension_path += "," + no_google_analytics_folder_path
        if os.path.exists(no_ad_folder_path):
            load_extension_path += "," + no_ad_folder_path
        if len(load_extension_path) > 0:
            options.add_argument('--load-extension=' + load_extension_path[1:])

    options.add_argument('--disable-features=TranslateUI')
    options.add_argument('--disable-translate')
    options.add_argument('--lang=zh-TW')

    options.add_argument("--password-store=basic")
    options.add_experimental_option("prefs", {"credentials_enable_service": False, "profile.password_manager_enabled": False})

    caps = options.to_capabilities()
    caps["unhandledPromptBehavior"] = u"accept"

    driver = None
    if os.path.exists(chromedriver_path):
        print("Use user driver path:", chromedriver_path)
        # driver = uc.Chrome(service=chrome_service, options=options, suppress_welcome=False)
        is_local_chrome_browser_lower = False
        try:
            driver = uc.Chrome(executable_path=chromedriver_path, options=options, desired_capabilities=caps,
                               suppress_welcome=False)
        except Exception as exc:
            if "cannot connect to chrome" in str(exc):
                if "This version of ChromeDriver only supports Chrome version" in str(exc):
                    is_local_chrome_browser_lower = True
            print(exc)
            pass

        if is_local_chrome_browser_lower:
            print("Use local user downloaded chromedriver to lunch chrome browser.")
            driver_type = "selenium"
            driver = load_chromdriver_normal(webdriver_path, driver_type, adblock_plus_enable)
    else:
        print("Oops! web driver not on path:", chromedriver_path)
        print('let uc automatically download chromedriver.')
        driver = uc.Chrome(options=options, desired_capabilities=caps, suppress_welcome=False)

    if driver is None:
        print("create web drive object fail!")
    else:
        download_dir_path = "."
        params = {
            "behavior": "allow",
            "downloadPath": os.path.realpath(download_dir_path)
        }
        # print("assign setDownloadBehavior.")
        driver.execute_cdp_cmd("Page.setDownloadBehavior", params)
    # print("driver capabilities", driver.capabilities)

    return driver

def galaxy_main(driver, url):
    # ignore url redirect
    # https://ticketing.galaxymacau.com/shows/show.aspx?sh=YGTTEV
    # if '/shows' in url:
    #     return

    try:
        window_handles_count = len(driver.window_handles)
        if window_handles_count > 1:
            driver.switch_to.window(driver.window_handles[0])
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
    except Exception as excSwithFail:
        pass

    # if '/eventDetail?' in url:
    #     is_modal_dialog_popup = check_modal_dialog_popup(driver)
    #     if is_modal_dialog_popup:
    #         print("is_modal_dialog_popup! skip...")
    #     else:
    #         date_auto_select_enable = config_dict["tixcraft"]["date_auto_select"]["enable"]
    #         if date_auto_select_enable:
    #             cityline_purchase_button_press(driver, config_dict)
    #
    # if '/performance?' in url:
    #     is_modal_dialog_popup = check_modal_dialog_popup(driver)
    #     if is_modal_dialog_popup:
    #         print("is_modal_dialog_popup! skip...")
    #     else:
    #         area_auto_select_enable = config_dict["tixcraft"]["area_auto_select"]["enable"]
    #         if area_auto_select_enable:
    #             cityline_performance(driver, config_dict)

def main():

    driver = None
    driver = get_driver_by_config(driver_type="uc")
    last_url = ""

    while True:
        time.sleep(0.1)

        if driver is None:
            print("web driver not accessible!")
            break


        url = ""

        try:
            url = driver.current_url
        except NoSuchWindowException:
            # print('NoSuchWindowException at this url:', url )
            # print("last_url:", last_url)
            try:
                window_handles_count = len(driver.window_handles)
                if window_handles_count > 1:
                    driver.switch_to.window(driver.window_handles[0])
            except Exception as excSwithFail:
                pass
        except UnexpectedAlertPresentException as exc1:
            # PS: DON'T remove this line.
            is_verifyCode_editing = False
            print('UnexpectedAlertPresentException at this url:', url)
            # time.sleep(3.5)
            # PS: do nothing...
            # PS: current chrome-driver + chrome call current_url cause alert/prompt dialog disappear!
            # raise exception at selenium/webdriver/remote/errorhandler.py
            # after dialog disappear new excpetion: unhandled inspector error: Not attached to an active page
            is_pass_alert = False
            is_pass_alert = True
            if is_pass_alert:
                try:
                    driver.switch_to.alert.accept()
                except Exception as exc:
                    pass

        except Exception as exc:
            is_verifyCode_editing = False

            logger.error('Maxbot URL Exception')
            logger.error(exc, exc_info=True)

            # UnicodeEncodeError: 'ascii' codec can't encode characters in position 63-72: ordinal not in range(128)
            str_exc = ""
            try:
                str_exc = str(exc)
            except Exception as exc2:
                pass

            if len(str_exc) == 0:
                str_exc = repr(exc)

            exit_bot_error_strings = [u'Max retries exceeded'
                , u'chrome not reachable'
                , u'unable to connect to renderer'
                , u'failed to check if window was closed'
                , u'Failed to establish a new connection'
                , u'Connection refused'
                , u'disconnected'
                , u'without establishing a connection'
                , u'web view not found'
                                      ]
            for each_error_string in exit_bot_error_strings:
                # for python2
                # say goodbye to python2
                '''
                try:
                    basestring
                    if isinstance(each_error_string, unicode):
                        each_error_string = str(each_error_string)
                except NameError:  # Python 3.x
                    basestring = str
                '''
                if isinstance(str_exc, str):
                    if each_error_string in str_exc:
                        print(u'quit bot')
                        driver.quit()
                        sys.exit()
                        break

            # not is above case, print exception.
            print("Exception:", str_exc)
            pass

        if url is None:
            continue
        else:
            if len(url) == 0:
                continue

        if 'galaxymacau.com' in url:
            galaxy_main(driver, url)
        # print(driver.current_url)

if __name__ == "__main__":
    main()