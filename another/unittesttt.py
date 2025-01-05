import time
from appium import webdriver
from typing import Any, Dict, sys
from appium.options.common import AppiumOptions
from appium.options.android import UiAutomator2Options

from appium.webdriver.common.appiumby import AppiumBy
import sys, time
sys.path.append("../TelegramAuto")
 
from watchlog import Watchlog
watchlog_instance = Watchlog()
# from devices.A71New import url, cap
# url = 'http://localhost:4721'

# cap: Dict[str, Any] = {
#     'platformName': 'Android',
#     'automationName': 'uiautomator2',
#     'deviceName': 'SamsungA71',
#     "platformVersion": "13.0",
#     'language': 'en',
#     'locale': 'us'
# }

# cap: Dict[str, Any] = {
#     'platformName': 'Android',
#     'automationName': 'uiautomator2',
#     'deviceName': 'SamsungA71',
#     "platformVersion": "13.0",
#     'language': 'en',
#     'locale': 'us'
# }
# appium_server = 'http://localhost:4721'

# desired_caps: Dict[str, Any] = {
#     'platformName': 'Android',
#     'automationName': 'uiautomator2',
#     'deviceName': 'SamsungA71',
#     "platformVersion": "13.0",
#     'language': 'en',
#     'locale': 'us'
# }
# appium_options = UiAutomator2Options().load_capabilities(desired_caps)
# driver_SamsungA71 = webdriver.Remote(appium_server, options=appium_options)

    
 
 
 
watchlog_instance.increment('Account_AddTo_PlusMesenger')
time.sleep(2)
# driver_SamsungA71.press_keycode(3)
 
    
