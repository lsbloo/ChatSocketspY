import socket

class Client(object):

    def __init__(self,host,port,name):
        self.port=port
        self.host=host
        self.tcp = self.createClient()
        self.name = name

    def __str__(self):
        return self.name

    def createClient(self):
        client_dest = (self.host,self.port)
        tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        tcp.connect(client_dest)
        return tcp

    def senderMSG(self,msg):
        self.tcp.send(msg)
        print("msg sender!")








