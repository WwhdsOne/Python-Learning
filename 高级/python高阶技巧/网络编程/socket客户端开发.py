import socket
# 创建socket对象
socket_client = socket.socket()
# 绑定IP和端口
socket_client.connect(("localhost",8888))
# 发送消息
while True:
    msg = input("请输入要发送的消息:")
    socket_client.send(msg.encode("utf-8"))
    if msg == "exit":
        break
    data = socket_client.recv(1024)
    print("接收到的消息为:",data.decode("utf-8"))
# 关闭连接
socket_client.close()