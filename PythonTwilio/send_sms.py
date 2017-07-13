from twilio.rest import Client

'''Send Sms using your own python code !!


This program sends a sms with the help of twilio.
For using it , you need to register with twilio @- https://www.twilio.com/try-twilio

Follow simple steps:-
	1. Create an account.
	2. Verify your phone number and email id.
	3. Buy a number for yourself with the free credits.
	4. Get this code.
	5. From your account copy the account sid and the auth token.
	6. Use those values in the code.
	7. Write your message in the code.
	8. Use your own number and the twilio number in the code and run it.

You'll get an sms from the twilio number with your message.'''



# Your Account SID from twilio.com/console
account_sid = "AC.................<your account sid>"
# Your Auth Token from twilio.com/console
auth_token  = ".................<your auth token>"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="<your number with country code>", 
    from_="<your twilio number with country code>",
    body="Hello from Python!")

print(message.sid)
