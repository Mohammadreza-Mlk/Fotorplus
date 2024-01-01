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
 }

url = 'http://localhost:4723'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
time.sleep(1)

for i in range(2):

    nameAccount = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.EditText')
    nameAccount.send_keys('lg;')
    time.sleep(1)
    nextB = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@content-desc="Done"]/android.view.View')
    nextB.click()

time.sleep(5)

driver.quit()
