import requests
import json,time

def CancelNumber(activationId):
     
    headers = {'activationId': f'{activationId}'}
        
    CancelBuyPoneNumberApi = 'https://fotorplusapi.membersgram.com/cancelPurchase'
    CancelBuyRequest = requests.get(CancelBuyPoneNumberApi, headers=headers)

    time.sleep(2)
    print(CancelBuyRequest.text)
    ResponseCancelBuyRequest = json.loads(CancelBuyRequest.text).get("status") 
    print(ResponseCancelBuyRequest)
    
# if CancelBuyRequest.text.status == "ACCESS_CANCEL":
#     print(CancelBuyRequest.text)
     
# else:
#     time.sleep(10)
#     CancelBuyRequest = requests.get(CancelBuyPoneNumberApi, headers=headers)
#     print(CancelBuyRequest.text)
# فراخوانی تابع GetNumber

