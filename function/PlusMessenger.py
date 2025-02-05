import time
from appium import webdriver
from typing import Any, Dict, sys
from appium.options.common import AppiumOptions
from appium.options.android import UiAutomator2Options

from appium.webdriver.common.appiumby import AppiumBy
import sys, time
sys.path.append("../TelegramAuto")
from function.UnistallApp import UnistalTelegram
from function.installTelegram import InstallTelegram
from function.ClearNotif import ClearNotif
from function.permission import Permission
from function.SaleToFotor import SaleFotor
from watchlog import Watchlog
watchlog_instance = Watchlog()

# from devices.A71New import url, cap
url = 'http://localhost:4721'

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'SamsungA71',
    "platformVersion": "13.0",
    'language': 'en',
    'locale': 'us'
}

def PlusMessanger(driver_SamsungA71, phoneNumber, TelegramApp):
    try:
        time.sleep(2)
        driver_SamsungA71.press_keycode(3)
        time.sleep(2)
                
        PlusMessage = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@content-desc="Plus"]')
        time.sleep(2)
        PlusMessage.click()
        time.sleep(2)
        try:
            NotificationError = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                    value='//android.widget.TextView[@text="Turn on notifications"]')
            if NotificationError:
                time.sleep(2)
                driver_SamsungA71.tap([(550, 900)])
        except:
            print("Notif not found")
        try:
            time.sleep(5)
            Themes = driver_SamsungA71.find_element(by=AppiumBy.XPATH,value='//android.widget.TextView[@text="Themes"]')
            if Themes:
                    time.sleep(2)
                    Cancel =   driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                            value='//android.widget.TextView[@text="Cancel"]') 
                    Cancel.click()                                

        except:
            print('')
        time.sleep(2)
        NavigationMenu = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.ImageView[@content-desc="Open navigation menu"]')
        NavigationMenu.click()
        # time.sleep(4)
        # touch.tap(x=70, y=160).release().perform()
        time.sleep(4)
        try:
            AddAccount = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                                value='//android.widget.TextView[@text="Add Account"]')
            
            AddAccount.click()
            time.sleep(4)
            
            NumberInput = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                                value='//android.widget.EditText[@content-desc="Country code"]')
            time.sleep(4)
            NumberInput.send_keys(phoneNumber)
            # print("1")
            # time.sleep(4)
            
            time.sleep(3)
            NextButton = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                                value='//android.widget.FrameLayout[@content-desc="Done"]/android.view.View')
            time.sleep(4)
            NextButton.click()
            time.sleep(4)
            confirmButton = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                                value='//android.widget.TextView[@text="Yes"]')
            time.sleep(4)
            confirmButton.click()
            time.sleep(4)
            print("waite for code")
            time.sleep(4)
            driver_SamsungA71.press_keycode(3)
            time.sleep(5)
            
            ClearNotif(driver_SamsungA71)
            driver_SamsungA71.implicitly_wait(4)
            TelegramApp = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                                    value='//android.widget.TextView[@content-desc="Telegram"]')
            time.sleep(4)
            TelegramApp.click()


            time.sleep(5)
            SearchButton = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                                    value='//android.widget.ImageButton[@content-desc="Search"]/android.widget.ImageView')
            SearchButton.click()
            time.sleep(4)
            SearchInput = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                                    value='//android.widget.EditText[@text="Search"]')
            SearchInput.send_keys("telegram ")
            time.sleep(5)
            driver_SamsungA71.tap([(400, 350)])

            ##########
            ##########
            time.sleep(3)
            # press on the final telegram message
            driver_SamsungA71.execute_script('mobile: longClickGesture', {'x': 500, 'y': 1800, 'duration': 1000})
            # touch.long_press(x=500, y=1800).release().perform()
            time.sleep(4)
            # tap on copy icon
            driver_SamsungA71.tap([(750, 170)])
            time.sleep(4)
            print("code copied")
            MessageBox = driver_SamsungA71.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Message"]')
            MessageBox.click()
            time.sleep(2)
            element_coord = MessageBox.location
            driver_SamsungA71.execute_script('mobile: longClickGesture', {'x': element_coord['x']+5, 'y': element_coord['y']+5, 'duration': 1500})
            #   touch.long_press(MessageBox).release().perform()
            time.sleep(1)
            driver_SamsungA71.tap([(150, 1240)])
            # touch.tap(x=150, y=1240).release().perform()

            time.sleep(2)
            print("message pasted")
            time.sleep(2)
            for m in range(60):
                # location of mark massage to delete
                driver_SamsungA71.long_press_keycode(67)
            time.sleep(2)   
            driver_SamsungA71.tap([(460, 1070)])
            time.sleep(2)
            driver_SamsungA71.execute_script('mobile: longClickGesture', {'x': 460, 'y': 1072, 'duration': 1000})
            time.sleep(2)
            driver_SamsungA71.tap([(430, 970)])
            time.sleep(2)
            driver_SamsungA71.press_keycode(3)
            time.sleep(2)
            driver_SamsungA71.press_keycode(3)
            time.sleep(2)   
            PlusMessage = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                    value='//android.widget.TextView[@content-desc="Plus"]')
            time.sleep(2)
            PlusMessage.click()
            time.sleep(2)
            driver_SamsungA71.execute_script('mobile: longClickGesture', {'x': 320, 'y': 1077, 'duration': 900})
            time.sleep(2)
            driver_SamsungA71.tap([(320, 930)])
            time.sleep(1.5) 
            watchlog_instance.increment('Account_AddTo_PlusMesenger')
            time.sleep(19)    
            try:
                NotificationError = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                        value='//android.widget.TextView[@text="Turn on notifications"]')
                if NotificationError:
                    time.sleep(2)
                    driver_SamsungA71.tap([(550, 900)])
                    
            except:
                print("Notif not found")
            time.sleep(2)
            driver_SamsungA71.press_keycode(3)
            time.sleep(8)
            ClearNotif(driver_SamsungA71)
            UnistalTelegram(driver_SamsungA71)
            time.sleep(4)
            InstallTelegram(driver_SamsungA71)
        except:
            SaleFotor(driver_SamsungA71)
    except:
        SaleFotor(driver_SamsungA71)       
