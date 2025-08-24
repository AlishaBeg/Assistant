# Assistant

python use to develope this (Artificial Logical Interface Support Human Activities)

### execute app script

```bash
cd Assistant
python app.py
```
<!-- 
###### SERVER SCRIPT

```
import socket

__HOST = '127.0.0.1'    # ip address

__PORT = 5000           # port number

# socket as (IPv4 and TCP)

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind socket with ip address and port

SOCKET.bind((Server.__HOST, Server.__PORT))

# Active server and listen connection with number or client (limit)

SOCKET.listen(5)

# This function run server loop or handle client    

connect, address = SOCKET.accept()

# Get request of client

response = input(' server response : ').encode()

connect.sendall(response)

# Send response to connected client 

request = connect.recv(1024).decode()

print(f'- client request : {request}')

# close client connection

connect.close()

# Close server SOCKET

SOCKET.close()

```
###### CLIENT SCRIPT

```
import socket

__HOST = '127.0.0.1'    # ip address

__PORT = 5000           # port number

# socket as (IPv4 and TCP)

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect with (server) use ip and and port number 

SOCKET.connect((Server.__HOST, Server.__PORT))

# Listen server response  

request = SOCKET.recv(1024).decode()

print(f'- server response : {request}')

# Send client request

response = input(' client request : ').encode()

SOCKET.sendall(response)

# close client connection

SOCKET.close()

# Close server SOCKET

SOCKET.close()

``` -->