from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import time

import random

url = 'http://localhost:4720'

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

Account_names_Lists = ["रित्विक", "आयुष", "समय", "अव्यक्त", "रेयांश", "परम", "कियान", "हृदान", "निवान", "आथर्व", "Serdar", "Gurbanguly", "Meret", "Döwlet", "Aman", "Nurmuhammet", "Maksat", "Arslan", "Atajan", "Çarymyrat", "Hoja", "Döwran", "Atamyrat", "Saparmyrat", "Yagşymyrat", "Suleyman", "Begmyrat", "Rejep", "Gorogly", "Ishanguly", "Çagamyrat", "Rovşen", "Baýram", "Balamyrat", "Döwranşa", "Durmuhammet", "Alym", "Garay", "Nazar", "Nebi", "Magtymguly", "Tagan", "Rejepguly", "Seyitmuhammet", "Kakajan", "Göçli", "Döwletgeldi", "Gün", "Azat", "Berdi", "Ata", "Gahryman", "Köçli", "Bolat", "Geldi", "Şageldi", "Çygyldam", "Muhammet", "Berdymyrat", "Wepa", "Gurban", "Nazarguly", "Myrat", "Durdi", "Atamyrat", "Bazar", "Allamyrat", "Zarif", "Chary", "Akmurat", "Jemşid", "Çolak", "Şiraly", "Garay", "Rejepmyrat", "Magtymgeldi", "Öwez", "Ata", "Dayanch", "Çelebi", "Emir", "Kerem", "Arda", "Can", "Ali", "Selim", "Ege", "Umut", "Baran", "Burak", "Deniz", "Yusuf", "Oğuz", "Kaan", "Mete", "Berk", "Cem", "Taylan", "Serkan", "Eren", "Ömer", "Alp", "Kuzey", "Kaya", "Orhan", "Hakan", "Mert", "Levent", "Volkan", "Tolga", "Serdar", "Ertan", "Ferit", "lker", "Taner", "Emre", "Onur", "Halit", "Ilgın", "Akın", "Aarav", "Aryan", "Aditya", "Arjun", "Rohan", "Siddharth", "Akshay", "Virat", "Kunal", "Varun", "Aakash", "Rahul", "Dev", "Harsh", "Yash", "Aniket", "Kabir", "Rishi", "Arnav", "Karan", "Shivansh", "Jayden", "Ansh", "Vihaan", "Vedant", "Parth", "Krish", "Advait", "Ayaan", "Dhruv", "Neil", "Raghav", "Kabir", "Aadi", "Vivaan", "Arush", "Tanish", "Omkar", "Advik", "Shaurya", "Ishan", "Rehan", "Anshuman", "Vihaan", "Zayn", "Shreyansh", "Aarush", "Aryan", "Arnav", "Lakshya", "Adam", "Jakub", "Kacper", "Szymon", "Mateusz", "Michał", "Filip", "Aleksander", "Mikołaj", "Wojciech", "Paweł", "Jan", "Wiktor", "Igor", "Alan", "Adrian", "Patryk", "Damian", "Oskar", "Artur", "Łukasz", "Bartosz", "Piotr", "Daniel", "Krzysztof", "Marcel", "Hubert", "Tomasz", "Dominik", "Sebastian", "Kamil", "Dawid", "Jacek", "Rafał", "Karol", "Sławomir", "Grzegorz", "Igor", "Radosław", "Dariusz", "Łukasz", "Marek", "Bogdan", "Zbigniew", "Jarosław", "Aleks", "Konrad", "Krystian", "Arkadiusz", "Edward", "Erkan", "Cihan", "Tarkan", "Gokhan", "Serhat", "Sinan", "Kaan", "Murat", "Oktay", "Arif", "आरव", "आर्यन", "आदित्य", "अर्जुन", "रोहन", "सिद्धार्थ", "अक्षय", "विराट", "कुणाल", "वरुण", "आकाश", "राहुल", "देव", "हर्ष", "यश", "अनिकेत", "कबीर", "रिषि", "अर्णव", "करण",  "शिवांश", "जेडन", "आंश", "विहान", "वेदांत", "पार्थ", "कृष", "आद्वैत", "आयान", "ध्रुव",  "नील", "रघव", "कबीर", "आदि", "विवान", "आरुष", "तनिष", "ओमकार", "अद्विक", "शौर्य",  "ईशान", "रेहन", "आंशुमान", "विहान", "ज़यन", "श्रेयांश", "आरुष", "आर्यन", "अर्णव", "लक्ष्य",  "अर्थ", "हृदय", "रुद्र", "सार्थक", "ईश्वर", "आरुष", "अविनाश", "आरुष", "प्रणव", "विहान", "सर्वेश", "पारस", "आदित्य", "रुद्रांश", "रिषभ", "अभिनव", "वंश", "अंशुल", "दक्ष", "आर्य", "अंशिका", "आदर्श", "आर्यमान", "सुर्यांश", "श्लोक", "रिषित", "अनय", "युवराज", "आद्वय", "यथार्थ", "Geldi", "Azat", "Gochmyrat", "Amanmyrat", "Hojaguly", "Döwletmyrat", "Mälim", "Täçberdi", "Dayanç", "Göroglu", "Nury", "Begench", "Myrat", "Mämmed", "Annasoltan", "Täzel", "Begmyrat", "Ylham", "Bashim", "Atageldi"]
# ایجاد آرایه اسم تصادفی برای اکانت
RandomAccountNames = random.sample(Account_names_Lists, 330)


# Start get number and create account
for i in range(8):
    print(f"{Fore.YELLOW}------- SAMSUNG J5 FOR {i} ----------- ")

    ChooseRandomIp = np.array([3, 2, 1])
    random_choice = np.random.choice(ChooseRandomIp)
    print("RandomIP = ", random_choice)
    driver_samsung_j5.press_keycode(3)
    time.sleep(2)
    MatsutiApp = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@text="Matsuri"]')
    MatsutiApp.click()
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
            touch.tap(x=910, y=1366).release().perform()
            time.sleep(1)
            touch.tap(x=910, y=1129).release().perform()
            time.sleep(1)

            try:
                VerificationInputBoxCodeTelegram = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                                  value='//android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[1]')

                if VerificationInputBoxCodeTelegram:
                    print("Phone Number IS Ok")
                    ##############
                    print("Phone Number IS Ok")
                    # گرفتن کد از Api
                    TelegramVerifyCode = ''

                    ##############
                    # وارد کردن کد
                    VerificationInputBoxCodeTelegram.send_keys(TelegramVerifyCode)

                    ##############
                    ##############
                    ##############
                    ##############
                    ##############
                    ##############
                    ##############
                    ##############

                    # چک کردن وجود داشتن باکس نام
                    try:

                        NAmeInput = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                   value='//android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.EditText')
                        if NAmeInput:
                            random_names = RandomAccountNames[i]
                            print(f'name tis account is : {random_names}')
                            time.sleep(0.5)
                            NAmeInput.send_keys(random_names)

                            NAmeInputNextButton = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                                 value='//android.widget.FrameLayout[@content-desc="Done"]/android.view.View')
                            NAmeInputNextButton.click()

                            # در بعضی کد کشور ها بعد از ثبت نام  یک ترم آف سرویس میاورد

                            try:

                                TermOfService = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                               value='//android.widget.TextView[@text="Terms of Service"]')
                                if TermOfService:
                                    TermOfServiceAccept = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
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

    driver_samsung_j5.press_keycode(3)
    time.sleep(2)

    #####################################
    #  محل قرار گیری مراحل فروش اکانت ـ ##
    #####################################
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
            touch.tap(x=910, y=1366).release().perform()
            time.sleep(1)
            touch.tap(x=910, y=1129).release().perform()
            time.sleep(1)

            try:
                VerificationInputBoxCodeTelegram = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                                  value='//android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[1]')

                if VerificationInputBoxCodeTelegram:
                    print("Phone Number IS Ok")
                    ##############
                    print("Phone Number IS Ok")
                    # گرفتن کد از Api
                    TelegramVerifyCode = ''

                    ##############
                    # وارد کردن کد
                    VerificationInputBoxCodeTelegram.send_keys(TelegramVerifyCode)

                    ##############
                    ##############
                    ##############
                    ##############
                    ##############
                    ##############
                    ##############
                    ##############

                    # چک کردن وجود داشتن باکس نام
                    try:

                        NAmeInput = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                   value='//android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.EditText')
                        if NAmeInput:
                            random_names = RandomAccountNames[i]
                            print(f'name tis account is : {random_names}')
                            time.sleep(0.5)
                            NAmeInput.send_keys(random_names)

                            NAmeInputNextButton = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                                 value='//android.widget.FrameLayout[@content-desc="Done"]/android.view.View')
                            NAmeInputNextButton.click()

                            # در بعضی کد کشور ها بعد از ثبت نام  یک ترم آف سرویس میاورد

                            try:

                                TermOfService = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                               value='//android.widget.TextView[@text="Terms of Service"]')
                                if TermOfService:
                                    TermOfServiceAccept = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
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

    driver_samsung_j5.press_keycode(3)
    time.sleep(2)

    #######################

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
    try:
        PhoneNumberInput = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                          value='//android.widget.EditText[@content-desc="Country code"]')

        if PhoneNumberInput:
            print("PhoneNumberInput found! Start phone number giving")
            # get phone number of API

            PhoneNumberInput.send_keys("989165540584")
            # click On next
            time.sleep(1)
            touch.tap(x=910, y=1366).release().perform()
            time.sleep(1)
            touch.tap(x=910, y=1129).release().perform()
            time.sleep(1)

            try:
                VerificationInputBoxCodeTelegram = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                                  value='//android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[1]')

                if VerificationInputBoxCodeTelegram:
                    print("Phone Number IS Ok")
                    ##############
                    print("Phone Number IS Ok")
                    # گرفتن کد از Api
                    TelegramVerifyCode = ''

                    ##############
                    # وارد کردن کد
                    VerificationInputBoxCodeTelegram.send_keys(TelegramVerifyCode)

                    ##############
                    ##############
                    ##############
                    ##############
                    ##############
                    ##############
                    ##############
                    ##############

                    # چک کردن وجود داشتن باکس نام
                    try:

                        NAmeInput = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                   value='//android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.EditText')
                        if NAmeInput:
                            random_names = RandomAccountNames[i]
                            print(f'name tis account is : {random_names}')
                            time.sleep(0.5)
                            NAmeInput.send_keys(random_names)

                            NAmeInputNextButton = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                                 value='//android.widget.FrameLayout[@content-desc="Done"]/android.view.View')
                            NAmeInputNextButton.click()

                            # در بعضی کد کشور ها بعد از ثبت نام  یک ترم آف سرویس میاورد

                            try:

                                TermOfService = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
                                                                               value='//android.widget.TextView[@text="Terms of Service"]')
                                if TermOfService:
                                    TermOfServiceAccept = driver_samsung_j5.find_element(by=AppiumBy.XPATH,
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

    time.sleep(2)

    #####################################
    #  محل قرار گیری مراحل فروش اکانت ـ ##
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
    for loopForCopyVerifyCode in range(2):
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
