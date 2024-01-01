from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import time
import json
import requests
import random

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Android',
    'language': 'en',
    'locale': 'us'
}
url = 'http://localhost:4723'
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

touch = TouchAction(driver)

try:
    PhoneNumberInput = driver.find_element(by=AppiumBy.XPATH,
                                           value='//android.widget.EditText[@content-desc="Country code"]')

    if PhoneNumberInput:
        print("PhoneNumberInput found! Start phone number giving")
        # پروسه گرفتن شماره از ای پی آی

        PhoneNumberInput.send_keys("16603455472")

        # click On next
        time.sleep(1)
        touch.tap(x=910, y=1366).release().perform()
        time.sleep(1)
        touch.tap(x=910, y=1129).release().perform()
        time.sleep(1)
        ####################
        ####################
        ####################
        ####################
        ####################
        ############
        try:
            VerificationCodeTelegram = driver.find_element(by=AppiumBy.XPATH,
                                                           value='//android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[1]')

            if VerificationCodeTelegram:
                print("Phone Number IS Ok")
                # پروسه دریافت کد تلگرام
                VerificationCodeTelegram.send_keys("0")

            else:
                try:
                    PhoneNumberBanned = driver.find_element(by=AppiumBy.XPATH,
                                                            value='//android.widget.TextView[@text="This phone number is banned."]')

                    if PhoneNumberBanned:
                        okButtonBanned = driver.find_element(by=AppiumBy.XPATH,
                                                             value='//android.widget.TextView[@text="OK"]')
                        print("PhoneNumberBanned")
                        okButtonBanned.click()

                        BackspaceButton = driver.find_element(by=AppiumBy.XPATH,
                                                              value='//android.view.ViewGroup/android.widget.ImageView')

                        for i in range(15):
                            BackspaceButton.click()
                except Exception as e:
                    print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")


except Exception as e:
    print(f"Error: {e}")

