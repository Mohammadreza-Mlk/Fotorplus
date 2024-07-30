from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import sys, time
sys.path.append("../TelegramAuto")
from function.checkForCallingCode import check_For_Calling_Code
from function.check_for_send_verify_code_to_another_telegram_sesseion import check_for_send_verify_code_to_another_telegram_sesseion
from function.Email_check import Email_check
from function.GetNumberAndGetCodeApi import GetNumberApi
from function.PhoneNumberIsBan import PhonenNumberBan
from function.CheckVerfiCodeSms import Check_Verify_code
from function.NameAccount import RandomName
from function.TooManyAttempts import TooManyAttempts
from function.FotorPlus import FotorPlus
from function.LogOut import LogOut


def Permission(driver_SamsungA71):

    touch = TouchAction(driver_SamsungA71)

    time.sleep(3)
    TelegamApp = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@content-desc="Telegram"]')
    time.sleep(3)
    touch.long_press(TelegamApp).release().perform()

    time.sleep(2.5)
    
    # TelegamApp = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
    #                                             value='//android.widget.TextView[@content-desc="Telegram"]')

    # time.sleep(3)
    # touch.long_press(TelegamApp).release().perform()

    # time.sleep(3)
    

    AppInfo = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.ImageView[@content-desc="App info"]')
    time.sleep(2.5)
    AppInfo.click()

    time.sleep(2.5)
    Permision = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@resource-id="android:id/title" and @text="Permissions"]')
    time.sleep(2.5)
    Permision.click()
    time.sleep(2.5)
    contact = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@resource-id="android:id/title" and @text="Contacts"]')
    time.sleep(2.5)
    contact.click()

    time.sleep(2.5)
    AlowPermission = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.RadioButton[@resource-id="com.android.permissioncontroller:id/allow_radio_button"]')
    AlowPermission.click()
    time.sleep(2.5)
    driver_SamsungA71.press_keycode(4)
    time.sleep(2.5)

    start_x = 800
    start_y = 800  
    end_x = 801  
    end_y = 200  
    touch.press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release().perform()


    time.sleep(2.5)
    notif = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@resource-id="android:id/title" and @text="Notifications"]')
    time.sleep(2.5)
    notif.click()
    time.sleep(2.5)
    notifAllow = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@resource-id="com.android.settings:id/switch_text"]')
    time.sleep(2.5)
    notifAllow.click()
    driver_SamsungA71.press_keycode(4)
    time.sleep(2.5)
    PhotosAndVideo = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@resource-id="android:id/title" and @text="Photos and videos"]')
    time.sleep(2.5)
    PhotosAndVideo.click()

    time.sleep(2.5)
    AlowPermissionPhotosAndVideo = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.RadioButton[@resource-id="com.android.permissioncontroller:id/allow_radio_button"]')
    AlowPermissionPhotosAndVideo.click()
    for i in range (3) : 
        driver_SamsungA71.press_keycode(4)
    

    time.sleep(3)  
    
    TelegamApp.click()
    try:
        driver_SamsungA71.implicitly_wait(15)  
        AppUpdateTelegram  = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@resource-id="android:id/alertTitle"]')
    
     
        if AppUpdateTelegram:
            
            AskMeInDay = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                    value='//android.widget.Button[@resource-id="android:id/button2"]')
            time.sleep(3)
            AskMeInDay.click()
    except:
        print("")
    
    
