# 请打开netAssist.exe
# https://github.com/nicedayzhu/netAssist/releases
import socket
socket_server = socket.socket()
# 绑定IP和端口
socket_server.bind(("127.0.0.1",8888)) 
# 监听
socket_server.listen(1)
conn , addr = socket_server.accept()
print("接收到连接请求,客户端地址为:",addr)
while True:
    data = conn.recv(1024).decode("utf-8")
    print("接收到的消息为:",data)
    if data == "exit":
        break
    reply = input("请输入回复消息:").encode("utf-8")
    conn.send(reply)
# 关闭连接
conn.close()
# 关闭服务端
socket_server.close()

