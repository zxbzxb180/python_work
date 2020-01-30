# socket服务端
import socket
import threading

server = socket.socket()

# 绑定到0.0.0.0:8000端口
server.bind(('0.0.0.0', 8000))
server.listen()


def handle_sock(sock, addr):
    while True:
        tmp_data = sock.recv(1024)
        if tmp_data:
            print(tmp_data.decode('utf8'))
        else:
            break

# 获取客户端连接并启动线程处理
while True:
    # 阻塞，等待连接
    sock, addr = server.accept()
    # 启动一个线程
    client_thread = threading.Thread(target=handle_sock, args=(sock,addr))
    client_thread.start()


