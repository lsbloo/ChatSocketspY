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




a = Server(4002,'127.0.0.1')
print(a.__str__())
tcp = a.createConnect(1)
while True:
    c, client = tcp.accept()
    print("Connect", client.__str__())
    while True:
        msg = c.recv(1024)
        if not msg: break
        print(client, msg)
    




