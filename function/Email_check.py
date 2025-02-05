from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import time, random
 
cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'SamsungA71',
    "platformVersion": "13.0",
    'language': 'en',
    'locale': 'us'
}
url = 'http://localhost:4721'
# driver_SamsungA71 = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))


def Email_check(driver_SamsungA71, TelegramApp):
    time.sleep(1)
    try:
        print("check another Email registered Before")
        time.sleep(1)
        AnotherEmailRegister = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.TextView[@text="Check Your Email"]')
        if AnotherEmailRegister:
            time.sleep(3)
            backButton = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.ImageView[@content-desc="Back"]')
            time.sleep(1)
            backButton.click()
            time.sleep(3)
            BackspaceButton = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                    value='//android.view.ViewGroup/android.widget.ImageView')

            for BackspaceButtonCount in range(15):
                driver_SamsungA71.long_press_keycode(67)
            
    except:
        print("another Email registered Before")
    
    try:
        time.sleep(2)
        try:
            NeedEmail = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@text="Choose a login email"]')
        except:
            print()
        try:
            NeedEmail = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@text="Add Email"]')
        except:
            print()

        if NeedEmail:
            time.sleep(3)
            NumberOfEmail = [1, 2, 3, 4, 5]
            randomEmail = random.choice(NumberOfEmail) 

            Email = f"pnxdevices{randomEmail}@gmail.com"
            print(Email)
            EmailInput = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.EditText')
        
            EmailInput.send_keys(Email)
            time.sleep(2)
            nextEmailButtun = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.FrameLayout[@content-desc="Done"]/android.view.View')
            nextEmailButtun.click()
            time.sleep(2)
            veifyCodeEmail = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                            value='//android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[1]')
            if veifyCodeEmail:
                driver_SamsungA71.press_keycode(3)
        
        try:
            time.sleep(10)
            gmailApp=''
            gmailApp = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@content-desc="Gmail"]')
            time.sleep(1)
            gmailApp.click()
        except:
            print(" gmail not found")
        try:
            time.sleep(10)
            gmailAppNotif = None
            gmailAppNotif= driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@content-desc="Gmail, 1 notification"]')
            time.sleep(1)
            gmailAppNotif.click()
        except:
            print(" gmail notif not found")
        if gmailAppNotif or gmailApp :
            
            time.sleep(1)
            driver_SamsungA71.tap([(960, 180)])
            time.sleep(2)
            try:
                EmailForGetCode = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value=f'//android.widget.TextView[@resource-id="com.google.android.gm:id/og_secondary_account_information" and @text="{Email}"]')
                EmailForGetCode.click()
            except:
                print("")
            try:
                EmailForGetCodeTitle = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value=f'//android.widget.TextView[@resource-id="com.google.android.gm:id/og_secondary_account_information" and @text="{Email}"]')
                if EmailForGetCodeTitle:
                    time.sleep(2)
                    close = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                                 value='//android.widget.ImageView[@content-desc="Close"]')
                    close.click()
            except:
                print("")
            time.sleep(3)
            try:
                tryNotif = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                                value='//android.widget.TextView[@resource-id="com.google.android.gm:id/item_list_card_title"]')
                if tryNotif:
                    time.sleep(3)
                    NotanksButton = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                                value='//android.widget.Button[@resource-id="com.google.android.gm:id/item_list_card_second_text_button"]')
                    NotanksButton.click()
            except:
                print("")
            driver_SamsungA71.tap([(500, 500)])
            time.sleep(3)
            
            driver_SamsungA71.execute_script('mobile: longClickGesture', {'x':385, 'y': 820, 'duration': 1000})

            time.sleep(3)
            driver_SamsungA71.tap([(150, 780)])
            time.sleep(2)

            Back_in_email_chat = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                                value='//android.widget.ImageButton[@content-desc="Navigate up"]')
            Back_in_email_chat.click()
            driver_SamsungA71.press_keycode(3)
            time.sleep(1.5)

            TelegramApp = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                                value='//android.widget.TextView[@content-desc="Telegram"]')
            TelegramApp.click()
            time.sleep(2)
            driver_SamsungA71.execute_script('mobile: longClickGesture', {'x':270, 'y': 950, 'duration': 1000})
            time.sleep(1)
            driver_SamsungA71.tap([(240, 824)])
            
                    
            # EmailNotAllowed = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
            #                                                             value='//android.widget.TextView[@text="An error occurred.EMAIL_NOT_ALLOWED"]')      
            # if EmailNotAllowed:
            #     print("Email Not Allowed")
            #     ################
            #     #################
            #     ###############
            #     # نوشتن کلیک  اوکی 
                
            #     time.sleep(3)
            #     NumberOfEmail = [1, 2, 3, 4, 5]
            #     randomEmail = random.choice(NumberOfEmail) 

            #     Email = f"pnxdevices{randomEmail}@gmail.com"
            #     print(Email)
            #     EmailInput = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
            #                                     value='//android.widget.EditText')
            
            #     EmailInput.send_keys(Email)
            #     time.sleep(2)
            #     nextEmailButtun = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
            #                                     value='//android.widget.FrameLayout[@content-desc="Done"]/android.view.View')
            #     nextEmailButtun.click()
            #     time.sleep(2)
            #     veifyCodeEmail = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
            #                                     value='//android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText[1]')
            #     if veifyCodeEmail:
            #         driver_SamsungA71.press_keycode(3)
            
            # try:
            #     time.sleep(10)
            #     gmailApp=''
            #     gmailApp = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
            #                                         value='//android.widget.TextView[@content-desc="Gmail"]')
            #     time.sleep(1)
            #     gmailApp.click()
            # except:
            #     print(" gmail not found")
            # try:
            #     time.sleep(10)
            #     gmailAppNotif = None
            #     gmailAppNotif= driver_SamsungA71.find_element(by=AppiumBy.XPATH,
            #                                         value='//android.widget.TextView[@content-desc="Gmail, 1 notification"]')
            #     time.sleep(1)
            #     gmailAppNotif.click()
            # except:
            #     print(" gmail notif not found")
            # if gmailAppNotif or gmailApp :
            #     time.sleep(5)
            #     touch.tap(x=960, y=180).release().perform()

            #     time.sleep(3)
            #     try:
            #         EmailForGetCode = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
            #                                         value=f'//android.widget.TextView[@resource-id="com.google.android.gm:id/og_secondary_account_information" and @text="{Email}"]')
            #         EmailForGetCode.click()
            #     except:
            #         print("")
            #     try:
            #         EmailForGetCodeTitle = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
            #                                         value=f'//android.widget.TextView[@resource-id="com.google.android.gm:id/og_secondary_account_information" and @text="{Email}"]')
            #         if EmailForGetCodeTitle:
            #             time.sleep(2)
            #             close = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
            #                                                         value='//android.widget.ImageView[@content-desc="Close"]')
            #             close.click()
            #     except:
            #         print("")
            #     time.sleep(3)

            #     touch.tap(x=500, y=500).release().perform()
            #     time.sleep(3)
                
                
            #     touch.long_press(x=385, y=840).release().perform()
            #     time.sleep(3)

            #     touch.tap(x=120, y=780).release().perform()
            #     time.sleep(3)

            #     Back_in_email_chat = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
            #                                                         value='//android.widget.ImageButton[@content-desc="Navigate up"]')
            #     Back_in_email_chat.click()
            #     driver_SamsungA71.press_keycode(3)
            #     time.sleep(2)

            #     AnotherEmail = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
            #                                                         value='//android.widget.TextView[@text="Check Your Email"]')
            
                
                
    except:
        print('need email not found')
        
        
