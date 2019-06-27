

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
    return receiver.senderMsgToReceiver(msg,getDataTCP(receiver),getDataTCP(sender))



def getDataTCP(client):
    host = ''
    process = ''
    receiver_data = client.tcp.__str__().split(",")
    for i in receiver_data[4]:
        if i.isdigit() or i == ".":
            host += i
    for j in receiver_data[5]:
        if j.isdigit():
            process += j

    result = (host, int(process))
    return result


def generateClient():
    client01 = createClients('osvaldo')
    client02 = createClients('maria')
    result = {"client01": client01 , "client02" : client02}
    return result


print("Digite [1] para enviar mensagem de um cliente para outro. ")
option = int(input())
if option == 1:
    result = generateClient()
    msg = str(input("Digite a mensagem que deseja enviar! > "))
    result_msg = str.encode(msg)

    print(senderMessenger(result,result_msg))






