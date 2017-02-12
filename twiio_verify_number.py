from twilio.rest import TwilioRestClient

# To find these visit https://www.twilio.com/user/account
ACCOUNT_SID = "AC4d42fc5c874e100bc43e99693f814971"
AUTH_TOKEN = "2f83f5e8f26c10d08e0c74a54a38853b"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
phone_number = raw_input("Enter your phone number: ")
response = client.caller_ids.validate(str(phone_number))
print response.get('validation_code')
