import socket
import threading



class Client(threading.Thread):

    def __init__(self,host,port,name):
        self.port=port
        self.host=host
        self.tcp = self.createClient()
        self.paramx = name



    def createClient(self):
        client_dest = (self.host,self.port)
        tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        tcp.connect(client_dest)
        return tcp

    def senderMSG(self,msg):
        self.tcp.send(msg)
        print("msg sender!")

    def senderMsgToReceiver(self,msg,receiver,sender):
        self.tcp.sendto(msg,receiver)
        exit = "Mensagem Enviada de " , sender ,  " Para: " , receiver
        return exit










