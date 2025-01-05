from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import sys, time
sys.path.append("../TelegramAuto")



def Permission(driver_SamsungA71):

 
    time.sleep(1)
    TelegramApp = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@content-desc="Telegram"]')
    
    element_coord = TelegramApp.location
    driver_SamsungA71.execute_script('mobile: longClickGesture', {'x': element_coord['x']+100, 'y': element_coord['y']+100, 'duration': 1100})

    time.sleep(2)    

    AppInfo = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.ImageView[@content-desc="App info"]')
    time.sleep(1)
    AppInfo.click()
    
    driver_SamsungA71.implicitly_wait(10)
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
     
    driver_SamsungA71.swipe(start_x, start_y, end_x, end_y, duration=200)


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
    
    TelegramApp.click()
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
    
    
