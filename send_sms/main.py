from twilio.rest import Client 
 
account_sid = '***********e8c3d7a18acf67c75c5eb3c' 
auth_token = '************22aa0ca29ce6abcd191644b' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='*********07b267def14e3aed7d818c', 
                              body='Hello there',      
                              to='(enter phone number)' 
                          ) 
 
print(message.sid)
