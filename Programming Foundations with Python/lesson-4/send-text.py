import twilio
import twilio.rest


# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# # Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC5021de58d8efd0098009c3a05c0b8773'
auth_token = 'cfb9db1c6e7d982eef6e0908c90ea1f3'
client = Client(account_sid, auth_token)

message = client.messages.create(
        body='Hello there!',
        from_='+15005550006',
        to='+84982997991'
    )

print(message.sid)