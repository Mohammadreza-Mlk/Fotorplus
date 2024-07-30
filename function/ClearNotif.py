from appium.webdriver.common.appiumby import AppiumBy
from typing import Any, Dict

def ClearNotif(driver_SamsungA71):
    start_x = 650
    end_x = 650
    start_y = 400
    end_y = 1000
    duration = 100  # مدت زمان سوایپ به میلی‌ثانیه

    driver_SamsungA71.swipe(start_x, start_y, end_x, end_y, duration)


    driver_SamsungA71.implicitly_wait(3)
    ClearButton = driver_SamsungA71.find_element(by=AppiumBy.XPATH,
                                                value='//android.widget.TextView[@content-desc="Clear,Button"]')

    ClearButton.click()