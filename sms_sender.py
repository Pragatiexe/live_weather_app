from twilio.rest import Client

ACCOUNT_SID = 'ACf1a6b7444792c1d599b2ba33cf06323c'
AUTH_TOKEN = '5e4767de3a6334c94337b6b4cb8ec7c8'
FROM_NUMBER ='+19787375752'  

def send_sms(to, message):
    try:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        client.messages.create(
            body=message,
            from_=FROM_NUMBER,
            to=to  
        )
        print("SMS sent successfully!")
    except Exception as e:
        print("SMS sending failed:", e)
        raise
