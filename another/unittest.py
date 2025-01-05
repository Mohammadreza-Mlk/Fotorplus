from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import sys, time, os
from appium.options.android import UiAutomator2Options

  
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
 
try:
    AddAccount = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                        value='//android.widget.TextView[@text="Add Account"]')
    print("addaccout")
        
    
except:

     
    driver_SamsungA71.press_keycode(3)
   
     