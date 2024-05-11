from _ast import expr
import requests
import json
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import time
import random
url = 'http://localhost:4721'

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'SamsungA71',
    "platformVersion": "13.0",
    'language': 'en',
    'locale': 'us'
}

driver_SamsungA71 = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
touch = TouchAction(driver_SamsungA71)

try:
    time.sleep(1)
    GetCodeInCall = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                         value='//*[starts-with(@text, "Calling")]')
    
    if GetCodeInCall:
        print("wait 75 sec")
        time.sleep(75)
        GetCodeInSms = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                         value='//android.widget.TextView[@text="Get the code via SMS"]')
        time.sleep(1)
        GetCodeInSms.click()
except:
    print('Calling not found')