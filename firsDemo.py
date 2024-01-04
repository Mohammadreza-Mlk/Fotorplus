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

OpenTelegramApp = driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.ImageView[@resource-id="com.mi.android.globallauncher:id/icon_icon"])[3]')
OpenTelegramApp.click()
time.sleep(2)

touch = TouchAction(driver)
for i in range(100000):
    # click on menu 3line(منوی 3 خط )
    touch.tap(x=103, y=129).release().perform()
    time.sleep(1)
    # click on arrow account
    touch.tap(x=490, y=490).release().perform()
    time.sleep(1)
    # click on add account
    touch.tap(x=490, y=730).release().perform()

    ##########
    ##########

    if True:

        urlRequestOne = 'https://5sim.net/v1/user/buy/activation/indonesia/virtual38/telegram'
        headers = {
                'Authorization':'Bearer eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzM3MjUwMDMsImlhdCI6MTcwMjE4OTAwMywicmF5IjoiMjAwN2ZmZjViOWZhZGUxNzI3YzI5M2FlMzg4YWM3MTkiLCJzdWIiOjIwMjkxMjZ9.vpvadx_XKONgmZpjr3IwOjxs8gUo1sXfGh65M3L4J9sWDdANgAwFb6e--c4_yxsqNGiUHrSIAOPI53aUoe_2yxknliC2sB2GLlHFMh_6BJZj2oYO_xyWnMcwFJr7lkfWjOf4TZkYtGJlfHJFxm3pfgN6n94dBGsLh6TuV8UypmzQZgTa-pAPFL973zcnpPwAJyUcvMo63WSKa0BI-KbvB8H8Vg9_PQYmpJ6p94OQgSme0DyqEVIAXhr0gh7PTs8WfFCbghrCUzW_uy28hQ1RgRvd7Os9P-cMzd8lE-hD2DftdhrJl8NEmHz6L2IUesFZZSLPPGtdct-fegtDnOlKRA',
                'Accept': 'application / json'}
        response = requests.get(urlRequestOne, headers=headers)

        if response.status_code == 200:
            print('درخواست موفقیت‌آمیز بود.')
            response_content = response.text  # ذخیره محتوای دریافتی در متغیر
            print('محتوای دریافتی: ', response_content)
            NumberOne = json.loads(response.text).get("phone")
            print(NumberOne)

            numberBox = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@content-desc="Country code"]')
            numberBox.send_keys(NumberOne)
            time.sleep(5)
            touch.tap(x=910, y=1366).release().perform()
            time.sleep(2)
            touch.tap(x=910, y=1129).release().perform()
            Id = (json.loads(response.text).get("آیدی"))
            time.sleep(20)
            url2 = f'https://5sim.net/v1/user/check/{Id}'
            response_code = requests.get(url2)
            code = 0
            if response_code.status_code == 200:
                if response_code.text.startswith("STATUS_OK"):
                    code = response_code.text.split(':')[1]
                    print(code)
            codeBox = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[1]')
            codeBox.send_keys(code)
            random_employe_names = random_employee_names[i]
            print(random_employe_names)
            print(" پیدا کردن اسم")
            nameAccount = driver.find_element(by=AppiumBy.CLASS_NAME, value='firstNameField')
                #touch.tap(x=524, y=713).release().perform())

            nameAccount.send_keys('lg;')

            time.sleep(2)
            # click on add account
            touch.tap(x=940, y=1194).release().perform()

        #######
        else:
            print(f'خطا در ارسال درخواست. کد وضعیت: {response.status_code}')
            print('محتوای خطا: ', response.text)
        time.sleep(1)
time.sleep(5)

driver.quit()
