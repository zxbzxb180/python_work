# qq客户端
import socket
import json
import threading

client = socket.socket()
client.connect(('127.0.0.1', 8000))

user = 'chenxi1'

# 1.登录
login_template = {
    'action': 'login',
    'user': user
}
client.send(json.dumps(login_template).encode('utf8'))
response = client.recv(1024)
print(response.decode('utf8'))

# 2.获取在线用户
get_user_template = {
    'action': 'list_user',
}
client.send(json.dumps(get_user_template).encode('utf8'))
response = client.recv(1024)
print('当前在线用户:{}'.format(response.decode('utf8')))

# 3.获取历史消息
offline_msg_template = {
    'action': 'history_msg',
    'user': user
}
client.send(json.dumps(offline_msg_template).encode('utf8'))
response = client.recv(1024)
print('历史消息:{}'.format(response.decode('utf8')))


def handle_send():
    while True:
        # 1. 随时可以发消息
        # 2. 有消息随时能收到
        op_type = input('请输入你要进行的操作：1、发送消息，2、获取在线用户，3、退出')
        if op_type not in ['1', '2', '3']:
            print('输入有误，请重新输入！')
            op_type = input('请输入你要进行的操作：1、发送消息，2、获取在线用户，3、退出')
        elif op_type == '1':
            to_user = input('请输入你要发送的用户：')
            msg = input('请输入你要发送的消息：')
            send_data_template = {
                'action': 'send_msg',
                'to': to_user,
                'from': user,
                'data': msg
            }
            client.send(json.dumps(send_data_template).encode('utf8'))
        elif op_type == '2':
            get_user_template = {
                'action': 'list_user'
            }
            client.send(json.dumps(get_user_template).encode('utf8'))
        elif op_type == '3':
            exit_template = {
                'action': 'exit',
                'user': user
            }
            client.send(json.dumps(exit_template).encode('utf8'))
            client.close()
            break


exit = False
def handle_receive():
    # 处理接收请求
    while True:
        if not exit:
            try:
                response = client.recv(1024)
            except:
                break
            response = response.decode('utf8')
            try:
                response_json = json.load(response)
                msg = response_json['data']
                from_user = response_json['from']
                print('')
                print('收到来自{0}的消息：{1}'.format(from_user, msg))
            except:
                print(response)
        else:
            break


if __name__ == '__main__':
    send_thread = threading.Thread(target=handle_send)
    receive_thread = threading.Thread(target=handle_receive)
    send_thread.start()
    receive_thread.start()