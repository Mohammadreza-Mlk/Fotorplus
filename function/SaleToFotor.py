from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

import sys, time
sys.path.append("../TelegramAuto")
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
   
def SaleFotor(driver_SamsungA71):
    for i in range(10):

        
        SearchButton = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                    value='//android.widget.ImageButton[@content-desc="Search"]/android.widget.ImageView')
        SearchButton.click()
        SearchInput = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                    value='//android.widget.EditText[@text="Search"]')
        SearchInput.send_keys("fotor_plus_bot")
        print("type fotor is ok")
        time.sleep(15)
        driver_SamsungA71.tap([(300, 400)])
        
        driver_SamsungA71.implicitly_wait(10)
        StartBot =  driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                    value='//android.widget.TextView[@text="START"]')
        StartBot.click()
        time.sleep(4)

        BotKeyBoard = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                    value='//android.widget.ImageView[@content-desc="Bot keyboard"]')
        BotKeyBoard.click()
        time.sleep(3)

        AccountVerify = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                    value='//android.widget.FrameLayout[@content-desc="Web tabs "]')
        AccountVerify.click()
        time.sleep(3)

        ShareContact = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                            value='//android.widget.TextView[@text="Share contact"]')
        ShareContact.click()


        time.sleep(20)

        BackButton = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                    value='//android.widget.ImageView[@content-desc="Go back"]')
        BackButton.click()
        time.sleep(10)
        SearchButton.click()
        SearchInput.send_keys("telegram")
        time.sleep(5)
        driver_SamsungA71.tap([(400, 300)])
    
        ##########
        ##########

        time.sleep(3)
        # press on the final telegram message
        driver_SamsungA71.execute_script('mobile: longClickGesture', {'x': 500, 'y': 1800, 'duration': 1000})
        time.sleep(4)
        # tap on copy icon
        driver_SamsungA71.tap([(630, 170)])
        time.sleep(2)
        print("code copied")
        BackButtonTelegramChat = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                                value='//android.widget.ImageView[@content-desc="Go back"]')
        BackButtonTelegramChat.click()
        time.sleep(2)

        SearchButton.click()
        time.sleep(2)

        SearchInput.send_keys("fotor_plus_bot")

        time.sleep(5)
        print("type fotor is ok")
        driver_SamsungA71.tap([(300, 400)])
        #######
        #######
        ######
        #########
        #########
        MessageBox = driver_SamsungA71.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Message"]')

        MessageBox.click()
        time.sleep(2)
        element_coord = MessageBox.location
        driver_SamsungA71.execute_script('mobile: longClickGesture', {'x': element_coord['x']+5, 'y': element_coord['y']+5, 'duration': 1500})

        time.sleep(1)
        driver_SamsungA71.tap([(150, 1240)])
    
        time.sleep(2)
        print("message pasted")
        time.sleep(2)
        # پاک کردن اضافه پیام برای نمایان شدن متن کد
        for m in range(60):
            
            driver_SamsungA71.long_press_keycode(67)
        time.sleep(1)   
        
        driver_SamsungA71.tap([(460, 1070)])
        time.sleep(1)

        
        driver_SamsungA71.execute_script('mobile: longClickGesture', {'x': 460, 'y': 1072, 'duration': 1000})
        time.sleep(1)
        driver_SamsungA71.tap([(270, 975)])

        
        
        MessageBox.send_keys("fotor_")
        # long press for open the menu for paste button
        driver_SamsungA71.execute_script('mobile: longClickGesture', {'x': 370, 'y': 1360, 'duration': 1000})
        # tap on paste button
        driver_SamsungA71.tap([(140, 1233)])
    
        time.sleep(1)
        SendButton = driver_SamsungA71.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Send"]')
        SendButton.click()
        time.sleep(2)
        driver_SamsungA71.tap([(64, 154)])
    
        watchlog_instance.increment('Account_AddTo_FotorBot')
        driver_SamsungA71.implicitly_wait(10)
        NavigationMenu = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                    value='//android.widget.ImageView[@content-desc="Open navigation menu"]')
        NavigationMenu.click()
        driver_SamsungA71.implicitly_wait(10)

        setting = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                    value='(//android.widget.TextView[@text="Settings"])[1]/android.view.View')
        setting.click()
        driver_SamsungA71.implicitly_wait(10)

        driver_SamsungA71.implicitly_wait(10)

        CircleForOpenMenu = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.ImageButton[@content-desc="More options"]/android.widget.ImageView')
        CircleForOpenMenu.click()
        driver_SamsungA71.implicitly_wait(10)
        LogOutInMenu = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                        value='//android.widget.TextView[@text="Log Out"]')
        driver_SamsungA71.implicitly_wait(10)
        LogOutInMenu.click()
        time.sleep(4)
        LogOutInMenu2 = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='(//android.widget.TextView[@text="Log Out"])[2]')
        LogOutInMenu2.click()
        driver_SamsungA71.implicitly_wait(10)
        LogOutInDialogBOx = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='(//android.widget.TextView[@text="Log Out"])[2]')
        LogOutInDialogBOx.click()
        print('sendin number to fotor is ✅✅✅✅')
        driver_SamsungA71.implicitly_wait(10)
