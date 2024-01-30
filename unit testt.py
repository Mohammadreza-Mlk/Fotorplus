from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import time
from colorama import Fore
import numpy as np

url = 'http://localhost:4720'

# Device 1 (Samsung)
capabilities_samsung_j5: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'platformVersion': '9.0',
    'deviceName': 'Samsung',
    'language': 'en',
    'locale': 'us'
}

driver_samsung_j5 = webdriver.Remote(url, options=AppiumOptions().load_capabilities(capabilities_samsung_j5))
touch = TouchAction(driver_samsung_j5)

# Common code for both devices
for i in range(50):

    print(f"{Fore.YELLOW}*********** *********** Start for on Samsung for{i} *********** *********** ")

    ChooseRandomIp = np.array([3, 2, 1])
    random_choice = np.random.choice(ChooseRandomIp)
    print("انتخاب آیپی تصادفی: ", random_choice)
    driver_samsung_j5.press_keycode(3)
    time.sleep(2)
    MatsutiApp_samsung = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                        value='//android.widget.TextView[@text="Matsuri"]')
    MatsutiApp_samsung.click()
    time.sleep(2)
    MatasuriIp = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                value=f'//android.widget.TextView[@text="new test{random_choice}"]')
    MatasuriIp.click()
    print("select Ip of Matsuri on Samsung")

    driver_samsung_j5.press_keycode(3)
    time.sleep(2)

    print(f"{Fore.GREEN}Find Telegram Google on Samsung")

    TelegramApp_google = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                        value='//android.widget.TextView[@text="Telegram"]')
    TelegramApp_google.click()
    print(f"{Fore.GREEN}Open Telegram Google on Samsung")

    time.sleep(3)

    # start creating an account
    StartMessage = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                  value='//android.widget.TextView[@text="Start Messaging"]')
    StartMessage.click()
    time.sleep(1)

    try:
        PhoneNumberInput = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                          value='//android.widget.EditText[@content-desc="Country code"]')

        if PhoneNumberInput:
            print("PhoneNumberInput found! Start phone number giving")
            # get phone number of API

            PhoneNumberInput.send_keys("989165540584")
            # click On next
            time.sleep(1)
            touch.tap(x=910, y=1200).release().perform()
            time.sleep(1)
            touch.tap(x=910, y=1200).release().perform()
            time.sleep(1)

            try:
                VerificationInputBoxCodeTelegram = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                                  value='//android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[1]')

                if VerificationInputBoxCodeTelegram:
                    print("Phone Number IS Ok")
                    # گرفتن کد از Api

                    # وارد کردن کد

                    #

                    #

                    # end create account
                # دکمه هوم گوشی

                # driver.press_keycode(3)
            except Exception as e:
                print(f"Error: verification code not find {e}")

            try:
                PhoneNumberBanned = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                   value='//android.widget.TextView[@text="This phone number is banned."]')

                if PhoneNumberBanned:
                    okButtonBanned = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                    value='//android.widget.TextView[@text="OK"]')
                    print("PhoneNumberBanned")
                    okButtonBanned.click()
                    BackspaceButton = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
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
    ###########################################
    # محل قرار گیری مراحل درخواست ای پی آی  ##
    ###########################################

    time.sleep(2)

    #####################################
    #  محل قرار گیری مراحل فروش اکانت ـ ##
    #####################################

    driver_samsung_j5.press_keycode(3)
    time.sleep(2)

    #######################

    print(f"{Fore.WHITE}Find Telegram Direct on Samsung")
    Folder_tel = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@text="Appium"]')
    Folder_tel.click()
    time.sleep(5)
    TelegramApp_Direct = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                        value='//android.widget.TextView[@text="Telegram"]')
    TelegramApp_Direct.click()
    print(f"{Fore.WHITE}Open Telegram Direct on Samsung")
    time.sleep(2)

    #####################################
    # محل قرار گیری مراحل ساخت اکانت ـ ##
    #####################################

    time.sleep(2)

    #####################################
    #  محل قرار گیری مراحل فروش اکانت ـ ##
    #####################################
    # start creating an account

    time.sleep(1)
    driver_samsung_j5.press_keycode(3)

    ###################################

    time.sleep(1)
    print(f"{Fore.RED}Find Telegram Beta on Samsung")

    TelegramApp_Beta = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                      value='//android.widget.TextView[@text="Telegram Beta"]')
    TelegramApp_Beta.click()
    print(f"{Fore.RED}Open Telegram Beta on Samsung")
    time.sleep(2)
    #####################################
    # محل قرار گیری مراحل ساخت اکانت ـ ##
    #####################################

    time.sleep(2)

    #####################################
    ##  محل قرار گیری مراحل فروش اکانت ـ ##
    #####################################

    time.sleep(16)
    SearchButton = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                  value='//android.widget.ImageButton[@content-desc="Search"]/android.widget.ImageView')
    SearchButton.click()
    SearchInput = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                 value='//android.widget.EditText[@text="Search"]')
    SearchInput.send_keys("fotor_plus_bot")
    FotorBot = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                              value='// android.view.ViewGroup[ @ text = "fotor, bot"]')
    FotorBot.click()
    # touch.tap(x=606, y=2023).release().perform()
    StartBotButton = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                    value='// android.widget.TextView[ @ text = "START"]')
    StartBotButton.click()
    BotKeyboard = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                 value='// android.widget.ImageView[ @ content - desc = "Bot keyboard"]')
    BotKeyboard.click()

    SellingAcc = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                value='// android.widget.TextView[ @ text = "Sending an account (selling an account)"]')
    SellingAcc.click()

    MessageBox = driver_samsung_j5.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Message"]')
    MessageBox.send_keys("989945873177")

    SendMessageIcon = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                     value='//android.view.View[@content-desc="Send"]')
    SendMessageIcon.click()
    BackButton = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                value='// android.widget.ImageView[ @ content - desc = "Go back"]')
    BackButton.click()

    SearchButton.click()

    SearchInput.send_keys("telegram")
    telegramChat = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                  value='//android.view.ViewGroup[@text="Telegram, Verified, support"]')
    telegramChat.click()

    ##########
    ##########

    time.sleep(3)
    # press on the final telegram message
    touch.long_press(x=500, y=1777).release().perform()
    # tap on copy icon
    touch.tap(x=724, y=164).release().perform()
    time.sleep(1)
    BackButton.click()

    SearchButton.click()

    SearchInput.send_keys("fotor_plus_bot")

    FotorBot.click()
    #######
    #######
    ######
    #########
    #########
    MessageBox.click()

    touch.long_press(x=245, y=1234).release().perform()

    touch.long_press(x=70, y=1068).release().perform()

    # location of mark massage to delete
    start_point = {'x': 154, 'y': 1129}
    startClearAll = {'x': 148, 'y': 1126}

    # انتها
    end_point = {'x': 812, 'y': 1238}
    endClearAll = {'x': 460, 'y': 1238}

    # پاک کردن اضافه پیام برای نمایان شدن متن کد
    for i in range(2):
        touch.long_press(x=start_point['x'], y=start_point['y']).move_to(x=end_point['x'],
                                                                         y=end_point['y']).release().perform()
        for j in range(3):
            touch.tap(x=994, y=1889).release().perform()
    touch.tap(x=473, y=1113).release().perform()
    touch.long_press(x=473, y=1113).release().perform()
    touch.tap(x=630, y=943).release().perform()
    touch.long_press(x=630, y=1113).release().perform()
    touch.tap(x=260, y=940).release().perform()
    touch.tap(x=994, y=1889).release().perform()
    MessageBox.send_keys("fotorplus_")
    # long press for open the menu for paste button
    touch.long_press(x=483, y=1225).release().perform()
    # tap on paste button
    touch.tap(x=425, y=1084).release().perform()
    time.sleep(1)
    SendButton = driver_samsung_j5.find_element(by=AppiumBy.XPATH, value='//android.view.View[@content-desc="Send"]')
    SendButton.click()

# Close both drivers when done
driver_samsung_j5.quit()
