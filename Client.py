@@ -0,0 +1,51 @@
import socket
import threading
import time

print("加载中")
time.sleep(1)
print("[###       ] 30%")
time.sleep(0.5)
print("[#####     ] 50%")
time.sleep(0.5)
print("[#######   ] 70%")
time.sleep(0.5)
print("[##########] 100%")
time.sleep(0.5)
print("加载成功！\n欢迎使用AR聊天室！")

class 聊天客户端:
    def __init__(self):
        self.用户名 = input("请输入你的名字：")
        self.服务器地址 = input("请输入服务器地址：")
        self.端口 = int(input("请输入服务器端口："))
        print("请多按几次Enter键，直到弹出欢迎语")

        self.客户端套接字 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.客户端套接字.connect((self.服务器地址, self.端口))

        threading.Thread(target=self.接收消息).start()
        self.发送消息()

    def 发送消息(self):
        while True:
            消息 = input()
            self.发送命令(f'{self.用户名}:{消息}')
            if 消息.lower() == 'exit':
                self.客户端套接字.close()
                break

    def 发送命令(self, 命令):
        self.客户端套接字.send(命令.encode('utf-8'))

    def 接收消息(self):
        while True:
            try:
                消息 = self.客户端套接字.recv(1024).decode('utf-8')
                print(消息)
            except:
                print("服务器已关闭")
                break

if __name__ == "__main__":
    客户端 = 聊天客户端()
