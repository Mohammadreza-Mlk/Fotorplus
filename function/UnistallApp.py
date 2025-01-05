from typing import Any, Dict
from appium.webdriver.common.appiumby import AppiumBy
import sys, time
sys.path.append("../TelegramAuto")

def UnistalTelegram(driver_SamsungA71):
        driver_SamsungA71.press_keycode(3)
        try:
                time.sleep(2)
                
                try:
                    time.sleep(2)
                    print("start to unistall")
                    # telegramBetaApp = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                    #                                         value='//android.widget.TextView[@content-desc="Telegram Beta"]')
                    time.sleep(2)
                    TelegramApp = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@content-desc="Telegram"]')
    
                    element_coord = TelegramApp.location
                    driver_SamsungA71.execute_script('mobile: longClickGesture', {'x': element_coord['x']+100, 'y': element_coord['y']+100, 'duration': 1100})

                        # driver_SamsungA71.execute_script('mobile: longClickGesture', {'x': 921, 'y': 1024, 'duration': 1000})
                     
                    time.sleep(2)
                    unistallTelegram = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                            value='//android.widget.FrameLayout[@content-desc="Uninstall, Button"]/android.widget.LinearLayout')
                    time.sleep(2)
                    unistallTelegram.click()
                    time.sleep(2)
                    confirmUnistall = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                            value='//android.widget.Button[@resource-id="android:id/button1"]')
                    time.sleep(2)
                    confirmUnistall.click()
                    if confirmUnistall:
                        print("unistall seccess")

                except:
                    print("telegram Beta app not found1")
        except:
                print("telegram Beta app not found 2")