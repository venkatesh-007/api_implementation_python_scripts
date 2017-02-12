from twilio.rest import TwilioRestClient

# To find these visit https://www.twilio.com/user/account
ACCOUNT_SID = "AC4d42fc5c874e100bc43e99693f814971"
AUTH_TOKEN = "2f83f5e8f26c10d08e0c74a54a38853b"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages.create(
    body="your phone number has been verified by us",  # Message body, if any
    to="+918652713385",
    from_="+17242692035",
)
print message.sid