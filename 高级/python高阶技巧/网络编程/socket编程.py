# Socket服务端编程
# 1. 创建socket对象
import socket
socker_server = socket.socket()
# 2. 绑定IP和端口
socker_server.bind(host,port)
# 3. 监听
socker_server.listen(backlog)
# backlog: 最大连接数,超过这个数会等待,不填写会自动填写一个合理值
# 4. 接收客户端连接
conn,addr = socker_server.accept()
print("接受到连接请求,客户端地址为:",addr)
# accept是一个阻塞方法,会等待客户端连接,连接后会返回一个元组,元组第一个元素是连接对象,第二个元素是客户端地址
# accept返回的是一个二元数组
# 5. 客户端连接后，通过recv方法，接收客户端发送的消息
while True:
    data = conn.recv(1024)
    # recv方法是一个阻塞方法,会等待客户端发送消息,接收到消息后会返回一个bytes类型的数据
    # 1024表示一次接收的最大字节数
    print("接收到的消息为:",data.decode("utf-8"))
    if data.decode("utf-8") == "exit": # 如果接收到的消息是exit,则退出循环
        break
# 6. 调用send方法,发送消息给客户端
    conn.send("消息已收到".encode("utf-8"))
# 7. conn（客户端当次连接对象）和socket_server对象调用close方法，关闭连接




