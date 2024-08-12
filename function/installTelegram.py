from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import sys, time
sys.path.append("../TelegramAuto")
from function.permission import Permission
cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'SamsungA71',
    "platformVersion": "13.0",
    'language': 'en',
    'locale': 'us'
}
url = 'http://localhost:4721'



def InstallTelegram(driver_SamsungA71):
    touch = TouchAction(driver_SamsungA71)
    driver_SamsungA71.implicitly_wait(3)
    print("Start Install telegram")
    time.sleep(4)
    driver_SamsungA71.tap([(165, 1385)])
     

    driver_SamsungA71.implicitly_wait(10) 
    InstallButton = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.Button[@resource-id="android:id/button1"]')
    
    InstallButton.click()
    time.sleep(15) 
    
    DoneButton = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.Button[@resource-id="android:id/button2"]')
    if DoneButton:
    #     print("DoneButton founde")
        
        DoneButton.click()
        print("telegram installed")
    # touch.tap(x=400, y=600).release().perform()
    # time.sleep(4)
    # touch.tap(x=400, y=600).release().perform()
    # time.sleep(4)

    start_x = 800
    start_y = 1200  
    end_x = 801  
    end_y = 500  
    driver_SamsungA71.swipe(start_x, start_y, end_x, end_y, duration=200)
 
    time.sleep(2)
    TelegramApp = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@content-desc="Telegram"]')
    element_coord = TelegramApp.location
    driver_SamsungA71.execute_script('mobile: longClickGesture', {'x': element_coord['x']+150, 'y': element_coord['y']+150, 'duration': 1500})
    # touch.long_press(TelegramApp).release().perform()
    time.sleep(2)
    
    Permission(driver_SamsungA71)
    # Permission(driver_SamsungA71, touch)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # time.sleep(4)
    # TelegamAppMenu = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
    #                                             value='//android.widget.TextView[@content-desc="Telegram"]')
    # time.sleep(4)
    # touch.long_press(TelegamAppMenu).release().perform()


    
    # TelegamApp = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
    #                                             value='//android.widget.TextView[@content-desc="Telegram"]')

    # time.sleep(4)
    # touch.long_press(TelegamApp).release().perform()

    # time.sleep(4)

    # AppInfo = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
    #                                             value='//android.widget.ImageView[@content-desc="App info"]')
    # time.sleep(4)
    # AppInfo.click()

    # time.sleep(4)
    # Permision = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
    #                                             value='//android.widget.TextView[@resource-id="android:id/title" and @text="Permissions"]')
    # time.sleep(4)
    # Permision.click()
    # time.sleep(4)
    # contact = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
    #                                             value='//android.widget.TextView[@resource-id="android:id/title" and @text="Contacts"]')
    # time.sleep(4)
    # contact.click()

    # time.sleep(4)
    # AlowPermission = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
    #                                             value='//android.widget.RadioButton[@resource-id="com.android.permissioncontroller:id/allow_radio_button"]')
    # AlowPermission.click()
    # time.sleep(4)
    # driver_SamsungA71.press_keycode(4)
    # time.sleep(4)

    # start_x = 800
    # start_y = 800  
    # end_x = 801  
    # end_y = 200  
    # driver_SamsungA71.swipe(start_x, start_y, end_x, end_y, duration=800)


    # time.sleep(4)
    # notif = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
    #                                             value='//android.widget.TextView[@resource-id="android:id/title" and @text="Notifications"]')
    # time.sleep(4)
    # notif.click()
    # time.sleep(4)
    # notifAllow = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
    #                                             value='//android.widget.TextView[@resource-id="com.android.settings:id/switch_text"]')
    # time.sleep(4)
    # notifAllow.click()
    # driver_SamsungA71.press_keycode(4)
    # time.sleep(4)
    # PhotosAndVideo = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
    #                                             value='//android.widget.TextView[@resource-id="android:id/title" and @text="Photos and videos"]')
    # time.sleep(4)
    # PhotosAndVideo.click()

    # time.sleep(4)
    # AlowPermissionPhotosAndVideo = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
    #                                             value='//android.widget.RadioButton[@resource-id="com.android.permissioncontroller:id/allow_radio_button"]')
    # AlowPermissionPhotosAndVideo.click()
    # for i in range (3) : 
    #     driver_SamsungA71.press_keycode(4)
    

    # time.sleep(4)  
    
    # TelegamApp.click()
    # try:
    #     driver_SamsungA71.implicitly_wait(15)  
    #     AppUpdateTelegram  = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
    #                                             value='//android.widget.TextView[@resource-id="android:id/alertTitle"]')
    
     
    #     if AppUpdateTelegram:
            
    #         AskMeInDay = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
    #                                                 value='//android.widget.Button[@resource-id="android:id/button2"]')
    #         time.sleep(4)
    #         AskMeInDay.click()
    # except:
    #     print("")
    
    
    # return TelegamApp