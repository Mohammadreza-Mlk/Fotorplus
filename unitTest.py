from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import time
import json
import requests
import random


Account_names = [
    "Emir", "Kerem", "Arda", "Can", "Ali", "Selim", "Ege", "Umut", "Baran", "Burak", "Deniz", "Yusuf", "Oğuz", "Kaan", "Mete", "Berk", "Cem", "Taylan", "Serkan", "Eren","Ömer", "Alp", "Kuzey", "Kaya", "Orhan", "Hakan", "Mert", "Levent", "Volkan", "Tolga",
    "Serdar", "Ertan", "Ferit", "lker", "Taner", "Emre", "Onur", "Halit", "Ilgın", "Akın", "Aarav", "Aryan", "Aditya", "Arjun", "Rohan", "Siddharth", "Akshay", "Virat", "Kunal", "Varun","Aakash", "Rahul", "Dev", "Harsh", "Yash", "Aniket", "Kabir", "Rishi", "Arnav", "Karan",
    "Shivansh", "Jayden", "Ansh", "Vihaan", "Vedant", "Parth", "Krish", "Advait", "Ayaan", "Dhruv", "Neil", "Raghav", "Kabir", "Aadi", "Vivaan", "Arush", "Tanish", "Omkar", "Advik", "Shaurya",
    "Ishan", "Rehan", "Anshuman", "Vihaan", "Zayn", "Shreyansh", "Aarush", "Aryan", "Arnav", "Lakshya", "Adam", "Jakub", "Kacper", "Szymon", "Mateusz", "Michał", "Filip", "Aleksander", "Mikołaj", "Wojciech", "Paweł", "Jan", "Wiktor", "Igor", "Alan", "Adrian", "Patryk", "Damian", "Oskar", "Artur", "Łukasz", "Bartosz", "Piotr", "Daniel", "Krzysztof", "Marcel", "Hubert", "Tomasz", "Dominik", "Sebastian", "Kamil", "Dawid", "Jacek", "Rafał", "Karol", "Sławomir", "Grzegorz", "Igor", "Radosław", "Dariusz", "Łukasz", "Marek", "Bogdan", "Zbigniew", "Jarosław", "Aleks", "Konrad", "Krystian", "Arkadiusz", "Edward",
    "Erkan", "Cihan", "Tarkan", "Gokhan", "Serhat", "Sinan", "Kaan", "Murat", "Oktay", "Arif", "आरव", "आर्यन", "आदित्य",
    "अर्जुन", "रोहन", "सिद्धार्थ", "अक्षय", "विराट", "कुणाल", "वरुण", "आकाश", "राहुल", "देव", "हर्ष", "यश", "अनिकेत",
    "कबीर", "रिषि", "अर्णव", "करण",  "शिवांश", "जेडन", "आंश", "विहान", "वेदांत", "पार्थ", "कृष", "आद्वैत", "आयान", "ध्रुव",  "नील", "रघव", "कबीर", "आदि", "विवान", "आरुष", "तनिष", "ओमकार", "अद्विक", "शौर्य",  "ईशान", "रेहन", "आंशुमान", "विहान", "ज़यन", "श्रेयांश", "आरुष", "आर्यन", "अर्णव", "लक्ष्य",  "अर्थ", "हृदय", "रुद्र", "सार्थक", "ईश्वर", "आरुष", "अविनाश", "आरुष", "प्रणव", "विहान", "सर्वेश", "पारस", "आदित्य", "रुद्रांश", "रिषभ", "अभिनव", "वंश", "अंशुल", "दक्ष", "आर्य", "अंशिका", "आदर्श", "आर्यमान", "सुर्यांश", "श्लोक", "रिषित", "अनय", "युवराज", "आद्वय", "यथार्थ",
    "रित्विक", "आयुष", "समय", "अव्यक्त", "रेयांश", "परम", "कियान", "हृदान", "निवान", "आथर्व", "Serdar", "Gurbanguly",
    "Meret", "Döwlet", "Aman", "Nurmuhammet", "Maksat", "Arslan", "Atajan", "Çarymyrat", "Hoja", "Döwran", "Atamyrat", "Saparmyrat", "Yagşymyrat", "Suleyman", "Begmyrat", "Rejep", "Gorogly", "Ishanguly",
    "Çagamyrat", "Rovşen", "Baýram", "Balamyrat", "Döwranşa", "Durmuhammet", "Alym", "Garay", "Nazar", "Nebi",
    "Magtymguly", "Tagan", "Rejepguly", "Seyitmuhammet", "Kakajan", "Göçli", "Döwletgeldi", "Gün", "Azat", "Berdi", "Ata", "Gahryman", "Köçli", "Bolat", "Geldi", "Şageldi", "Çygyldam", "Muhammet", "Berdymyrat", "Wepa", "Gurban", "Nazarguly", "Myrat", "Durdi", "Atamyrat", "Bazar", "Allamyrat", "Zarif", "Chary", "Akmurat",
    "Jemşid", "Çolak", "Şiraly", "Garay", "Rejepmyrat", "Magtymgeldi", "Öwez", "Ata", "Dayanch", "Çelebi",
    "Geldi", "Azat", "Gochmyrat", "Amanmyrat", "Hojaguly", "Döwletmyrat", "Mälim", "Täçberdi", "Dayanç", "Göroglu",
    "Nury", "Begench", "Myrat", "Mämmed", "Annasoltan", "Täzel", "Begmyrat", "Ylham", "Bashim", "Atageldi"]

# ایاد آرایه اسم تصادفی برای اکانت
RandomAccountNames = random.sample(Account_names, 330)


cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Android',
    'language': 'en',
    'locale': 'us'
}

url = 'http://localhost:4723'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
time.sleep(1)
touch = TouchAction(driver)

# Open telegram application
OpenTelegramApp = driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.ImageView[@resource-id="com.mi.android.globallauncher:id/icon_icon"])[3]')
OpenTelegramApp.click()
time.sleep(2)

for i in range(100000):
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
            RequestNumberOne = 'https://5sim.net/v1/user/buy/activation/england/virtual51/telegram'
            headers = {
                'Authorization': 'Bearer eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzM3MjUwMDMsImlhdCI6MTcwMjE4OTAwMywicmF5IjoiMjAwN2ZmZjViOWZhZGUxNzI3YzI5M2FlMzg4YWM3MTkiLCJzdWIiOjIwMjkxMjZ9.vpvadx_XKONgmZpjr3IwOjxs8gUo1sXfGh65M3L4J9sWDdANgAwFb6e--c4_yxsqNGiUHrSIAOPI53aUoe_2yxknliC2sB2GLlHFMh_6BJZj2oYO_xyWnMcwFJr7lkfWjOf4TZkYtGJlfHJFxm3pfgN6n94dBGsLh6TuV8UypmzQZgTa-pAPFL973zcnpPwAJyUcvMo63WSKa0BI-KbvB8H8Vg9_PQYmpJ6p94OQgSme0DyqEVIAXhr0gh7PTs8WfFCbghrCUzW_uy28hQ1RgRvd7Os9P-cMzd8lE-hD2DftdhrJl8NEmHz6L2IUesFZZSLPPGtdct-fegtDnOlKRA',
                'Accept': 'application / json'}
            response = requests.get(RequestNumberOne, headers=headers)

            if response.status_code == 200:
                print('درخواست موفقیت‌آمیز بود.')
                response_content = response.text  # ذخیره محتوای دریافتی در متغیر
                print('محتوای دریافتی: ', response_content)
                NumberOne = json.loads(response.text).get("phone")
                print(NumberOne)

                PhoneNumberInput.send_keys(NumberOne)

                # click On next
                time.sleep(1)
                touch.tap(x=910, y=1366).release().perform()
                time.sleep(1)
                touch.tap(x=910, y=1129).release().perform()
                time.sleep(1)
                ####################
                ####################
                ####################
                ####################
                ####################
                ############
                try:
                    VerificationInputBoxCodeTelegram = driver.find_element(by=AppiumBy.XPATH,
                                                                           value='//android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[1]')

                    if VerificationInputBoxCodeTelegram:
                        print("Phone Number IS Ok")
                        # پروسه دریافت کد تلگرام
                        SmsActive_Id = (json.loads(response.text).get("id"))
                        time.sleep(25)
                        RequestNumberOneVerifyCode = f'https://5sim.net/v1/user/check/{SmsActive_Id}'
                        response_code = requests.get(RequestNumberOneVerifyCode, headers=headers)
                        TelegramVerifyCode = 0
                        if response_code.status_code == 200:
                            if response_code.text.startswith("STATUS_OK"):
                                TelegramVerifyCode = response_code.text.split(':')[1]
                                print(TelegramVerifyCode)

                        VerificationInputBoxCodeTelegram.send_keys(TelegramVerifyCode)

                        RandomAccountNames = RandomAccountNames[i]
                        print(RandomAccountNames)
                        print(" پیدا کردن اسم")
                        NameAccount = driver.find_element(by=AppiumBy.XPATH,
                                                          value='//android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.EditText')
                        NameAccount.send_keys(RandomAccountNames)
                        time.sleep(1)
                        NextButton = driver.find_element(by=AppiumBy.XPATH,
                                                         value='//android.widget.FrameLayout[@content-desc="Done"]/android.view.View')
                        NextButton.click()

                        ##############################
                        ## End of create an account ##
                        ##############################

                    else:
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

                                for BackspaceButtonCount in range(15):
                                    BackspaceButton.click()
                        except Exception as e:
                            print(f"Error: {e}")
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print("محدود شدن در ثبت نام اکانت")
    except Exception as e:
        print(f"Error: محدود شدن در ثبت نام اکانت ----> {e}")
        time.sleep(25200)
