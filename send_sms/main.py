from twilio.rest import Client 
 
account_sid = '*********' 
auth_token = '************' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='*********', 
                              body='Hello there',      
                              to='(enter phone number)' 
                          ) 
 
print(message.sid)
