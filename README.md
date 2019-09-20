# Twilio based and Selenium based automated Whatsapp messaging programs
<p>
1. sending_message_twilio.py: is a Python program that sends Whatsapp messages to
any number that has subscribed to my sandbox client on Twilio. It uses a REST API call to send a Whatsapp message. <br />
To run:
<br />
python sending_message_twilio.py
<br />
<br />
2. sending_message_selenium.py: is a Python program that sends Whatsapp messages to any contact (individual or group) via Selenium. So this code opens a browser window, connects to Whastapp web, then asks you to scan you QR code and then automatically sends out the message.
To run:
<br />
python sending_message_selenium.py "This is a test message"
<br />
