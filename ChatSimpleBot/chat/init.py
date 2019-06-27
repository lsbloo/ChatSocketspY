

from ChatSimpleBot.chat.clientTCP import  Client
import re

list_clients=[]


def createClients(name_client):
    client = Client('127.0.0.1',4002,name_client)
    list_clients.append(client)
    return client

def senderMessenger(result,msg):
    receiver = result['client01']
    sender = result['client02']
    host=''
    process=''
    receiver_data = receiver.tcp.__str__().split(",")
    for i in receiver_data[4]:
        if i.isdigit() or i == ".":
            host +=i
    for j in receiver_data[5]:
        if j.isdigit():
            process+=j

    result = (host,int(process))

    sender.senderMsgToReceiver(msg,result)




client01_osvaldo = createClients('osvaldo')
client02_osvaldo2 = createClients('osvaldo2')

result = {"client01": client01_osvaldo , "client02" : client02_osvaldo2}

msg=b'mensagem enviada!'
senderMessenger(result,msg)




