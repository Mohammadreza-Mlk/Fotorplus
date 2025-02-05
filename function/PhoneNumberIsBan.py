from typing import Any, Dict
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import time

url = 'http://localhost:4721'

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'SamsungA71',
    "platformVersion": "13.0",
    'language': 'en',
    'locale': 'us'
}

# driver_SamsungA71 = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
def PhonenNumberBan(driver_SamsungA71):
     
    print("start Check Banned")
   
    try:
        time.sleep(2)
        PhoneNumberBanned = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@text="This phone number is banned."]')

        if PhoneNumberBanned:
            okButtonBanned = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                    value='//android.widget.TextView[@text="OK"]')
            print("PhoneNumberBanned")
            okButtonBanned.click()
            BackspaceButton = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                    value='//android.view.ViewGroup/android.widget.ImageView')

            for BackspaceButtonCount in range(2):
                element_coord = BackspaceButton.location
                driver_SamsungA71.execute_script('mobile: longClickGesture', {'x': element_coord['x']+1, 'y': element_coord['y']+1, 'duration': 1300})
            return True
    except :
        print("####  Phone number  is not banned ####")
        return False
        
        
        
def InvalidPhonenNumber(driver_SamsungA71):
     
    print("start Check Invalid")
     
    try:
        time.sleep(2)
        InvalidPhonenNumber = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@text="Invalid phone number. Please check the number and try again."]')

        if InvalidPhonenNumber:
            okButtonBanned = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                    value='//android.widget.TextView[@text="OK"]')
            print("InvalidPhonenNumber")
            okButtonBanned.click()
            time.sleep(1)
            BackspaceButton = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                    value='//android.view.ViewGroup/android.widget.ImageView')

            for BackspaceButtonCount in range(2):
                element_coord = BackspaceButton.location
                driver_SamsungA71.execute_script('mobile: longClickGesture', {'x': element_coord['x']+1, 'y': element_coord['y']+1, 'duration': 1300})
                # touch.long_press(BackspaceButton).wait(1).release().perform()
            return True
    except :
        print("####  Phone number  is True  ####")
        return False
    try:
        time.sleep(2)
        InvalidPhonenNumber = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@text="Wrong format"]')

        if InvalidPhonenNumber:
            okButtonBanned = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                    value='//android.widget.TextView[@text="OK"]')
            print("InvalidPhonenNumber")
            okButtonBanned.click()
            time.sleep(1)
            BackspaceButton = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                    value='//android.view.ViewGroup/android.widget.ImageView')

            for BackspaceButtonCount in range(2):
                element_coord = BackspaceButton.location
                driver_SamsungA71.execute_script('mobile: longClickGesture', {'x': element_coord['x']+1, 'y': element_coord['y']+1, 'duration': 1300})
                # touch.long_press(BackspaceButton).wait(1).release().perform()
            return True
    except :
        print("####  Phone number  is True  ####")
        return False
