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
for create_Account_Count in range(10000):
    for TelegramAppIndex in range(1, 4):
        # دکمه هوم گوشی
        driver.press_keycode(3)

        Telegram = driver.find_element(by=AppiumBy.XPATH,
                                       value=f'(//android.widget.ImageView[@resource-id="com.mi.android.globallauncher:id/icon_icon"])[{TelegramAppIndex}]')

        print(f"find telegram {TelegramAppIndex}")
        Telegram.click()
        print(f"open telegram {TelegramAppIndex}")
        # start creating an account
        StartMessage = driver.find_element(by=AppiumBy.XPATH,
                                           value='//android.widget.TextView[@text="Start Messaging"]')
        StartMessage.click()
        time.sleep(1)
        # click on arrow account

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

                                try:

                                    TermOfService = driver.find_element(by=AppiumBy.XPATH,
                                                                        value='//android.widget.TextView[@text="Terms of Service"]')
                                    if TermOfService:
                                        TermOfServiceAccept = driver.find_element(by=AppiumBy.XPATH,
                                                                                  value='//android.widget.TextView[@text="Accept"]')
                                        TermOfServiceAccept.click()
                                except Exception as e:
                                    print("Term of service not fount")
                        except Exception as e:
                            print("account created")

                        #

                        #

                        # end create account
                    # دکمه هوم گوشی

                    # driver.press_keycode(3)
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


