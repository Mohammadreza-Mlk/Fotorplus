from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
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
url = 'http://localhost:4721'


driver_SamsungA71 = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

# def Permission(driver_SamsungA71):
for i in range(10):
    touch = TouchAction(driver_SamsungA71)

    driver_SamsungA71.implicitly_wait(3)
    SearchButton = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.ImageButton[@content-desc="Search"]/android.widget.ImageView')
    SearchButton.click()
    SearchInput = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.EditText[@text="Search"]')
    SearchInput.send_keys("fotor_plus_bot")
    print("type fotor is ok")
    time.sleep(15)
    touch.tap(x=300, y=400).release().perform()
    time.sleep(5)
    StartBot =  driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@text="START"]')
    StartBot.click()
    time.sleep(5)

    BotKeyBoard = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.ImageView[@content-desc="Bot keyboard"]')
    BotKeyBoard.click()
    time.sleep(2)

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
    touch.tap(x=400, y=300).release().perform()

    ##########
    ##########

    time.sleep(3)
    # press on the final telegram message
    touch.long_press(x=500, y=1800).release().perform()
    time.sleep(4)
    # tap on copy icon
    touch.tap(x=630, y=170).release().perform()
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

    touch.tap(x=300, y=400).release().perform()
    #######
    #######
    ######
    #########
    #########
    MessageBox = driver_SamsungA71.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Message"]')

    MessageBox.click()
    time.sleep(2)

    touch.long_press(MessageBox).release().perform()
    time.sleep(1)

    touch.tap(x=150, y=1240).release().perform()

    time.sleep(2)
    print("message pasted")
    time.sleep(2)
    # پاک کردن اضافه پیام برای نمایان شدن متن کد
    for m in range(2):
        # location of mark massage to delete
        start_point = {'x': 160, 'y': 1220}
        end_point = {'x': 960, 'y': 1273}

        touch.long_press(x=start_point['x'], y=start_point['y']).move_to(x=end_point['x'], y=end_point['y']).release().perform()
        touch.tap(x=1000, y=2000).release().perform()
        touch.tap(x=1000, y=2000).release().perform()
        touch.tap(x=1000, y=2000).release().perform()

    touch.tap(x=440, y=1150).release().perform()
    touch.long_press(x=440, y=1145).release().perform()
    touch.tap(x=370, y=1035).release().perform()
    touch.tap(x=844, y=1280).release().perform()


    touch.long_press(x=1000, y=2000).release().perform()
    touch.long_press(x=1000, y=2000).release().perform()
    touch.long_press(x=1000, y=2000).release().perform()

    MessageBox.send_keys("fotor_")
    # long press for open the menu for paste button
    touch.long_press(x=370, y=1360).release().perform()
    # tap on paste button
    touch.tap(x=140, y=1233).release().perform()

    time.sleep(1)
    SendButton = driver_SamsungA71.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Send"]')
    SendButton.click()
    time.sleep(2)
    touch.tap(x=64, y=154).release().perform()

    watchlog_instance.increment('Account_AddTo_FotorBot')
    time.sleep(2)
    NavigationMenu = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.ImageView[@content-desc="Open navigation menu"]')
    NavigationMenu.click()
    time.sleep(2)

    setting = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='(//android.widget.TextView[@text="Settings"])[1]/android.view.View')
    setting.click()
    time.sleep(2)

    time.sleep(2)

    CircleForOpenMenu = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.ImageButton[@content-desc="More options"]/android.widget.ImageView')
    CircleForOpenMenu.click()
    time.sleep(2)
    LogOutInMenu = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                    value='//android.widget.TextView[@text="Log Out"]')
    time.sleep(2)
    LogOutInMenu.click()
    time.sleep(2)
    LogOutInMenu2 = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                        value='(//android.widget.TextView[@text="Log Out"])[2]')
    LogOutInMenu2.click()
    time.sleep(2)
    LogOutInDialogBOx = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='(//android.widget.TextView[@text="Log Out"])[2]')
    LogOutInDialogBOx.click()
    print('sendin number to fotor is ✅✅✅✅')
    time.sleep(2)
