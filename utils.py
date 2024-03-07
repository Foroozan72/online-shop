from kavenegar import *

def send_otp_code(phone_number , code):

    try:
        api = KavenegarAPI('35795977784A6951452B4D4F306145752F7374394B4E422F5A795A434F6E662F50316F2F6A31734F3361453D')
        params = {
            'sender': '',#optional
            'receptor': 'phone_number' ,#multiple mobile number, split by comma
            'message': ' {code} کد احراز شما  شرکت فروزان - فوریکا ',
        } 
        response = api.sms_send(params)
        print(response)
    except APIException as e: 
        print(e)
    except HTTPException as e: 
        print(e)