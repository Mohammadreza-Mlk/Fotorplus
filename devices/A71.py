from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import sys, time, os
from appium.options.android import UiAutomator2Options

sys.path.append("../TelegramAuto")

# اضافه کردن مسیر والد دایرکتوری جاری به sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from function.checkForCallingCode import check_For_Calling_Code
from function.installTelegram import InstallTelegram
from function.CallingNew import Calling
from function.check_for_send_verify_code_to_another_telegram_sesseion import check_for_send_verify_code_to_another_telegram_sesseion
from function.Email_check import Email_check
from function.GetNumberAndGetCodeApi import GetNumberApi
from function.PhoneNumberIsBan import PhonenNumberBan, InvalidPhonenNumber
from function.CheckVerfiCodeSms import Check_Verify_code
from function.NameAccount import RandomName
from function.TooManyAttempts import TooManyAttempts
from function.PlusMessenger import PlusMessanger
from function.FotorPlus import FotorPlus
from function.permission import Permission
from watchlog import Watchlog
watchlog_instance = Watchlog()

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'SamsungA71',
    "platformVersion": "13.0",
    'language': 'en',
    'locale': 'us'
}
appium_server = 'http://localhost:4721'

desired_caps: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'SamsungA71',
    "platformVersion": "13.0",
    'language': 'en',
    'locale': 'us'
}
appium_options = UiAutomator2Options().load_capabilities(desired_caps)
driver_SamsungA71 = webdriver.Remote(appium_server, options=appium_options)
   
# driver_SamsungA71 = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
touch = TouchAction(driver_SamsungA71)
phoneNumber = ""
activationId = ""
# Permission(driver_SamsungA71)
Check_Verify_code(driver_SamsungA71)