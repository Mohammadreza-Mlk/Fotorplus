import requests
import json
url = 'https://sms-activate.org/stubs/handler_api.php?api_key=0d53cff86Bf2B112505f22661656fe31&action=getNumberV2&service=tg&ref=2220188&country=6'
payload = {'param1': 'value1', 'param2': 'value2'}
# https://api.sms-activate.org/stubs/handler_api.php?api_key=0d53cff86Bf2B112505f22661656fe31&action=getStatus&id=1997693525
# STATUS_OK:512367

response = requests.get(url, params=payload)


if response.status_code == 200:
    print('درخواست موفقیت‌آمیز بود.')
    response_content = response.text  # ذخیره محتوای دریافتی در متغیر
    print('محتوای دریافتی: ', response_content)
    print(json.loads(response.text).get("phoneNumber"))
else:
    print(f'خطا در ارسال درخواست. کد وضعیت: {response.status_code}')
    print('محتوای خطا: ', response.text)
