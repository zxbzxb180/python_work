# socket客户端
import socket
client = socket.socket()
client.connect(('169.254.246.25', 8000))

while True:
    input_data = input()
    client.send(input_data.encode('utf8'))

# client.close()