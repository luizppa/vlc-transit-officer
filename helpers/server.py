import socket

from helpers.connection_controller import ConnectionController

class Server(ConnectionController):
    clients = []

    def serve(self, peers = 1):
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        origin = (self.host, self.port)
        tcp.bind(origin)
        tcp.listen(peers)
        for _i in range(0, peers):
            try:
                connection, client = tcp.accept()
                self.clients.append({
                    'connection': connection,
                    'client': client
                })
                print('Serving to ', client)
            except socket.timeout:
                print('Could not connect to all peers')
                return self.clients

        return self.clients

    def broadcast(self, message):
        for client in self.clients:
            client['connection'].send(message.encode('utf-8'))