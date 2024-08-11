from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from time import sleep

# Deprecated in warning status
from appium.webdriver.common.touch_action import TouchAction

# Deprecated in warning status
from appium.webdriver.common.multi_action import MultiAction

# W3C compatible: create more gestures
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.mouse_button import MouseButton

# W3C compatible: available as driver methods
from appium.webdriver.extensions.action_helpers import ActionHelpers

from helper import desired_caps

# =================================================================================
## Different ways to make gestures in appium:
# 1. "touch_action/multi_action" libraries (deprecated)
# 2. W3C Actions (action_builder library)
# 3. "action_helper" library (some already created w3c actions)
# 4. Mobile gestures
#   - (https://github.com/appium/appium-uiautomator2-driver/tree/master?tab=readme-ov-file#mobile-gesture-commands)
#   - (https://github.com/appium/appium-uiautomator2-driver/blob/master/docs/android-mobile-gestures.md)
# 5. Android UiScrollable Class (https://developer.android.com/reference/androidx/test/uiautomator/UiScrollable)
# 6. Appium Gesture Plugin (https://github.com/AppiumTestDistribution/appium-gestures-plugin)
# =================================================================================
## Difference between gestures:
# Tap: Use fingers
# Click: Use mouse
# Press: Use input device / Hold fingers on screen
# Scroll: From element to another element
# Swipe: From a point to another point (With duration - Release hand after it is done)
# Flick: From a point to another point (No control and duration - Release hand before it is done)
# =================================================================================
appium_server = "http://127.0.0.1:4723"
# >>> All `sleep`s are for demo purpose
# =================================================================================
# 0. Get element rect (bounds) - Location (Coordination - X,Y) | Size (Height, Width)
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.implicitly_wait(5) 
el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Animation')
print(el.rect)
print(el.location)
print(el.location_in_view)
driver.quit()

# =================================================================================
# 0. Get window rect/size (bounds) - Location (Coordination - X,Y) | Size (Height, Width)
appium_options = UiAutomator2Options().load_capabilities(desired_caps.apidemos)
driver = webdriver.Remote(appium_server, options=appium_options)
driver.implicitly_wait(5)
window_rect = driver.get_window_rect()
window_size = driver.get_window_size()
print(window_rect)
print(window_size)
driver.quit()



# =================================================================================
# 8. Press and Hold - TouchAction
appium_options = UiAutomator2Options().load_capabilities(desired_caps.contacts)
driver = webdriver.Remote(appium_server, options=appium_options)
contacts = driver.find_elements(by=AppiumBy.ID, value="com.android.contacts:id/cliv_name_textview")
actions = TouchAction(driver)

# actions.long_press(el=contacts[0]).perform()
# or:
actions.press(el=contacts[0]).wait(ms=1000).release().perform()
sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# 9. Press and Hold - Actions API - W3C
appium_options = UiAutomator2Options().load_capabilities(desired_caps.contacts)
driver = webdriver.Remote(appium_server, options=appium_options)
contacts = driver.find_elements(by=AppiumBy.ID, value="com.android.contacts:id/cliv_name_textview")
chains = ActionChains(driver)
chains.w3c_actions.pointer_action.click_and_hold(contacts[0])
chains.perform()
sleep(2)  # For demo purpose
driver.quit()

# =================================================================================
# 10. Press and Hold - Mobile Gesture Commands - W3C
appium_options = UiAutomator2Options().load_capabilities(desired_caps.contacts)
driver = webdriver.Remote(appium_server, options=appium_options)
contacts = driver.find_elements(by=AppiumBy.ID, value="com.android.contacts:id/cliv_name_textview")
element_coord = contacts[0].location
driver.execute_script('mobile: longClickGesture', {'x': element_coord['x'], 'y': element_coord['y'], 'duration': 1000})
sleep(2)  # For demo purpose
driver.quit()
