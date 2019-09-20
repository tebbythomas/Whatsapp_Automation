'''
Description:
Twilio Python program to send a whatsapp message to any contact that subscribes
to reveiving messages from the sandbox client
'''
from twilio.rest import Client

# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
client = Client()

# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+14155238886'
# replace this number with your own WhatsApp Messaging number
#to_whatsapp_number='whatsapp:+15005550006'
to_whatsapp_number='whatsapp:+919999999999'
client.messages.create(body='Hello Hello!',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)
