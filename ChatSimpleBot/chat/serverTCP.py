import socket



class Server(object):

    def __init__(self,port,host):
        self.port=port
        self.host=host
    def __str__(self):
        return 'server init!'

    def createConnect(self, amount):
        server_origin = (self.host,self.port)
        tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        tcp.bind(server_origin)
        tcp.listen(amount)
        return tcp




list_clients=[]

def start(amount):
    a = Server(4002,'127.0.0.1')
    print(a.__str__())
    tcp = a.createConnect(1)
    cont = 0
    while cont < amount:
        c, client = tcp.accept()
        print("Connect", client)
        list_clients.append(client)
        cont=cont+1
        show_msg(c,client)
    return list_clients


def show_msg(c,client):
    msg = c.recv(1024)
    print("Existe uma mensagem: " , msg , ":" , "Cliente : " , client)

start(1000)





