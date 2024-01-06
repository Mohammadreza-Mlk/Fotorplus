from _ast import expr

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import time
from NameAccount import Account_names, RandomAccountNames

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

# Open telegram application
# OpenTelegramApp = driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.ImageView[@resource-id="com.mi.android.globallauncher:id/icon_icon"])[3]')
# OpenTelegramApp.click()
# time.sleep(2)

for i in range(1000):
    # click on menu 3line(منوی 3 خط )
    touch.tap(x=102, y=128).release().perform()
    time.sleep(1)
    # click on arrow account
    touch.tap(x=490, y=490).release().perform()
    time.sleep(1)
    # click on add account
    touch.tap(x=490, y=730).release().perform()

    ##########
    ##########
    try:
        PhoneNumberInput = driver.find_element(by=AppiumBy.XPATH,
                                               value='//android.widget.EditText[@content-desc="Country code"]')

        if PhoneNumberInput:
            print("PhoneNumberInput found! Start phone number giving")
            # پروسه گرفتن شماره از ای پی آی

            PhoneNumberInput.send_keys("989165540584")

            # click On next
            time.sleep(1)
            touch.tap(x=910, y=1366).release().perform()
            time.sleep(1)
            touch.tap(x=910, y=1129).release().perform()
            time.sleep(1)

            try:
                VerificationInputBoxCodeTelegram = driver.find_element(by=AppiumBy.XPATH,
                                                                       value='//android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[1]')

                if VerificationInputBoxCodeTelegram:
                    print("Phone Number IS Ok")
                    # گرفتن کد از Api

                    # وارد کردن کد

                    # چک کردن وجود داشتن باکس نام
                    try:

                        NAmeInput = driver.find_element(by=AppiumBy.XPATH,
                                                        value='//android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.EditText')
                        if NAmeInput:
                            random_names = RandomAccountNames[i]
                            print(f'name tis account is : {random_names}')
                            time.sleep(0.5)
                            NAmeInput.send_keys(random_names)

                            NAmeInputNextButton = driver.find_element(by=AppiumBy.XPATH,
                                                                      value='//android.widget.FrameLayout[@content-desc="Done"]/android.view.View')
                            NAmeInputNextButton.click()

                            # در بعضی کد کشور ها بعد از ثبت نام  یک ترم آف سرویس میاورد
                            TermOfService = driver.find_element(by=AppiumBy.XPATH,
                                                                value='//android.widget.TextView[@text="Terms of Service"]')

                            TermOfServiceAccept = driver.find_element(by=AppiumBy.XPATH,
                                                                      value='//android.widget.TextView[@text="Accept"]')
                            TermOfServiceAccept.click()
                    except Exception as e:
                        print("account created")

                    #

                    #

                    # end create account

            except Exception as e:
                print(f"Error: verification code not find {e}")

            try:
                PhoneNumberBanned = driver.find_element(by=AppiumBy.XPATH,
                                                        value='//android.widget.TextView[@text="This phone number is banned."]')

                if PhoneNumberBanned:
                    okButtonBanned = driver.find_element(by=AppiumBy.XPATH,
                                                         value='//android.widget.TextView[@text="OK"]')
                    print("PhoneNumberBanned")
                    okButtonBanned.click()
                    BackspaceButton = driver.find_element(by=AppiumBy.XPATH,
                                                          value='//android.view.ViewGroup/android.widget.ImageView')

                    for BackspaceButtonCount in range(2):
                        touch.long_press(BackspaceButton).wait(1).release().perform()
            except Exception as e:
                print(f"Error: #### banned is not true #### {e}")
        else:
            print("محدود شدن در ثبت نام اکانت")
    except Exception as e:
        print(f"Error: محدود شدن در ثبت نام اکانت ----> {e}")
        time.sleep(25200)
