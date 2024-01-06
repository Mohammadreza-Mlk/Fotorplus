import requests
import json
import time

# RequestNumberOne = 'https://5sim.net/v1/user/buy/activation/england/virtual51/telegram'
headers = {
    'Authorization': 'Bearer eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzM3MjUwMDMsImlhdCI6MTcwMjE4OTAwMywicmF5IjoiMjAwN2ZmZjViOWZhZGUxNzI3YzI5M2FlMzg4YWM3MTkiLCJzdWIiOjIwMjkxMjZ9.vpvadx_XKONgmZpjr3IwOjxs8gUo1sXfGh65M3L4J9sWDdANgAwFb6e--c4_yxsqNGiUHrSIAOPI53aUoe_2yxknliC2sB2GLlHFMh_6BJZj2oYO_xyWnMcwFJr7lkfWjOf4TZkYtGJlfHJFxm3pfgN6n94dBGsLh6TuV8UypmzQZgTa-pAPFL973zcnpPwAJyUcvMo63WSKa0BI-KbvB8H8Vg9_PQYmpJ6p94OQgSme0DyqEVIAXhr0gh7PTs8WfFCbghrCUzW_uy28hQ1RgRvd7Os9P-cMzd8lE-hD2DftdhrJl8NEmHz6L2IUesFZZSLPPGtdct-fegtDnOlKRA',
    'Accept': 'application / json'}
#response = requests.get(RequestNumberOne, headers=headers)


SmsActive_Id = 547738644

RequestNumberOneVerifyCode = f'https://5sim.net/v1/user/check/{SmsActive_Id}'
response_code = requests.get(RequestNumberOneVerifyCode, headers=headers)

if response_code.status_code == 200:
    print(' موفقیت‌آمیز .')
    response_codeTe = response_code.text  # ذخیره محتوای دریافتی در متغیر
    print('محتوای دریافتی: ', response_codeTe)
    codeTel = json.loads(response_code.text).get("sms")
    print(codeTel)

