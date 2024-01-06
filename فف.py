from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import time

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Android',
    'language': 'en',
    'locale': 'us'
}

url = 'http://localhost:4723'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
touch = TouchAction(driver)
BackspaceButton = driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.view.ViewGroup/android.widget.ImageView')

for BackspaceButtonCount in range(2):
    touch.long_press(BackspaceButton).wait(1).release().perform()
    print(f'done{BackspaceButtonCount}')
