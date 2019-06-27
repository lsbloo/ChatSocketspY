
from chat.clientTCP import Client


b = Client('127.0.0.1',4002,'osvaldo')
msg = b'OLA'
b.senderMSG(msg)


