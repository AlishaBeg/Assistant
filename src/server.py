
class Server:

    def __init__(self, host="127.0.0.1", port=5000):

        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = {}
        self.block_list = {}

    def broadcast(self, sender, message):
        for user, connection in self.clients.item():
            if sender in self.block_list.get(user, set()):
                continue
            if user != sender:
                try:
                    connection.sendall(f"[{sender}] : {message}".encode())
                except:
                    pass

    def private_message(self, sender, receiver, message):

        connection = self.clients.get(receiver)

        if connection:
            if sender in self.block_list(receiver, set()):
                return
            try:
                connection.sendall(f"[PM from {sender}] : {message}".encode)
            except:
                pass

    def client_request(self, connection, address):
        try:
            connection.sendall(b"enter username : ")
            username = connection.recv(1024).decode().strip()

            if not username or username in self.clients:
                connection.sendall(b"invalid username")
                connection.close()
                return

            

        except Exception as err:
            print(f"[ERROR] : {err}")
        finally:
            if username in self.clients:
                del self.clients[username]
                del self.blocks[username]

                self.broadcast("SERVER", f"{username} is exit")
            connection.close()
            print(f"connection {address} is (closed)")