# -*- coding: utf-8 -*-
"""sms.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dkc7dodE_sKC4sYbU9hmdiUdpQbNCzH2
"""

!pip install twilio

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hi ',
                              from_='+17622543602',
                              status_callback='http://postb.in/1234abcd',
                              to='+xxxxxxxxx'
                          )

print(message.sid)

