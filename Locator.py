from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import time
from NameAccount import url, cap
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

PhoneNumberInput = driver.find_element(by=AppiumBy.XPATH,
                                       value='//android.widget.EditText[@content-desc="Country code"]')

okButtonBanned = driver.find_element(by=AppiumBy.XPATH,
                                     value='//android.widget.TextView[@text="OK"]')

BackspaceButton = driver.find_element(by=AppiumBy.XPATH,
                                      value='//android.view.ViewGroup/android.widget.ImageView')

PhoneNumberBanned = driver.find_element(by=AppiumBy.XPATH,
                                        value='//android.widget.TextView[@text="This phone number is banned."]')

