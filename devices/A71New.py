from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
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
   
phoneNumber = ""
activationId = ""
time.sleep(1)
TelegramApp = InstallTelegram(driver_SamsungA71) 
time.sleep(2)
print("start create Account")
for i in range(20):
    try:
        time.sleep(1)
        StartMessage = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                    value='//android.widget.TextView[@text="Start Messaging"]')
        StartMessage.click()
        print(" start button clicked")
    except:
        print("no start button")
    try:
        time.sleep(2)
        PhoneNumberInput = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                        value='//android.widget.EditText[@content-desc="Country code"]')
        if PhoneNumberInput:
            print("PhoneNumberInput found! Start phone number giving :)")
            
            phoneNumber,activationId = GetNumberApi()
            time.sleep(2)
            PhoneNumberInput.send_keys(phoneNumber)
            time.sleep(2)
            nextButton =   driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                        value='//android.widget.FrameLayout[@content-desc="Done"]/android.view.View')
            nextButton.click()  # click On next
            time.sleep(1)
            ConfirmNumberButton =   driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                                value='//android.widget.TextView[@text="Yes"]')
            ConfirmNumberButton.click()
            time.sleep(2)
        
    except:
        print("PhoneNumberInput not found")
    time.sleep(0.5)
    TooManyAttempts(driver_SamsungA71)
    time.sleep(0.5)
    InvalidPhonenNumber(driver_SamsungA71)
    time.sleep(0.5)
    resultBan = PhonenNumberBan(driver_SamsungA71)
    if not resultBan :
        time.sleep(3)
        Email_check(driver_SamsungA71, TelegramApp)

        time.sleep(3)
        anotherTelegram = check_for_send_verify_code_to_another_telegram_sesseion(driver_SamsungA71)
        if not anotherTelegram:
            
                time.sleep(1)
                print(activationId)
                resultCalling = Calling(driver_SamsungA71, activationId, phoneNumber)
                if not resultCalling:
                    
                    time.sleep(5)
                    resultCode = Check_Verify_code(driver_SamsungA71, phoneNumber , activationId)
                    if resultCode : 
                        RandomName(driver_SamsungA71)
                        time.sleep(6)
                        PlusMessanger(driver_SamsungA71, phoneNumber, TelegramApp)
        else:
            print("another telegram session in phone number")
