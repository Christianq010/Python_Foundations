from twilio.rest import TwilioRestClient

# Your Account SID from twilio.com/console
account_sid = "AC73ac26265d35d530b6520e958eef671f"
# Your Auth Token from twilio.com/console
auth_token  = "96282c733dcaeb054d25da5cd1615b8f"

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    to="+94777549947", 
    from_="+17244797232",
    body="This damn thing takes ages to arrive!")

print(message.sid)
