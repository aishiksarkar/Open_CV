# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure

def work(total):
    if total == 2:
        account_sid = "ACe1057a708e1837973376fe048ffd6c0b"
        auth_token = "4d649236e14d52d57ebbe5b4786d7298"
        client = Client(account_sid, auth_token)
        message = client.messages.create(
        body="Patient is hungry",
        from_="+15855774698",
        to="+917044563322"
        )
    elif total== 4:
        account_sid = "ACe1057a708e1837973376fe048ffd6c0b"
        auth_token = "4d649236e14d52d57ebbe5b4786d7298"
        client = Client(account_sid, auth_token)
        message = client.messages.create(
        body="Patient needs washroom",
        from_="+15855774698",
        to="+917044563322"
        )

