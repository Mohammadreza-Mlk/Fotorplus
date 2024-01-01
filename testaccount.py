from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import time
import json
import requests

urlRequestOne = 'https://5sim.net/v1/user/buy/activation/indonesia/virtual38/telegram'
headers = {
    'Authorization': 'Bearer eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzM3MjUwMDMsImlhdCI6MTcwMjE4OTAwMywicmF5IjoiMjAwN2ZmZjViOWZhZGUxNzI3YzI5M2FlMzg4YWM3MTkiLCJzdWIiOjIwMjkxMjZ9.vpvadx_XKONgmZpjr3IwOjxs8gUo1sXfGh65M3L4J9sWDdANgAwFb6e--c4_yxsqNGiUHrSIAOPI53aUoe_2yxknliC2sB2GLlHFMh_6BJZj2oYO_xyWnMcwFJr7lkfWjOf4TZkYtGJlfHJFxm3pfgN6n94dBGsLh6TuV8UypmzQZgTa-pAPFL973zcnpPwAJyUcvMo63WSKa0BI-KbvB8H8Vg9_PQYmpJ6p94OQgSme0DyqEVIAXhr0gh7PTs8WfFCbghrCUzW_uy28hQ1RgRvd7Os9P-cMzd8lE-hD2DftdhrJl8NEmHz6L2IUesFZZSLPPGtdct-fegtDnOlKRA',
    'Accept': 'application / json'}
response = requests.get(urlRequestOne, headers=headers)

if response.status_code == 200:
    print('درخواست موفقیت‌آمیز بود.')
    response_content = response.text  # ذخیره محتوای دریافتی در متغیر
    print('محتوای دریافتی: ', response_content)
    NumberOne = json.loads(response.text).get("phone")
    print(NumberOne)
