from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import time
import numpy as np


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
for create_Account_Count in range(10000):
    for TelegramAppIndex in range(1, 4):
        my_array = np.array([1, 2, 3])
        random_choice = np.random.choice(my_array)

        print("انتخاب تصادفی: ", random_choice)
        # دکمه هوم گوشی
        driver.press_keycode(3)

        Matsuri = driver.find_element(by=AppiumBy.XPATH,
                                      value='(//android.widget.ImageView[@resource-id="com.mi.android.globallauncher:id/icon_icon"])[4]')
        Matsuri.click()
        VPNIP = driver.find_element(by=AppiumBy.XPATH,
                                    value=f'(//android.widget.TextView[@resource-id="moe.matsuri.lite:id/profile_name"])[{random_choice}]')

        VPNIP.click()
        driver.press_keycode(3)

        Telegram = driver.find_element(by=AppiumBy.XPATH,
                                       value=f'(//android.widget.ImageView[@resource-id="com.mi.android.globallauncher:id/icon_icon"])[{TelegramAppIndex}]')

        print(f"find telegram {TelegramAppIndex}")
        Telegram.click()
        print(f"open telegram {TelegramAppIndex}")
        # start creating an account
        StartMessage = driver.find_element(by=AppiumBy.XPATH,
                                           value='//android.widget.TextView[@text="Start Messaging"]')
        StartMessage.click()
        time.sleep(1)
        # click on arrow account

        ##########
        ##########



