import socket
import time
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    massage = msg.encode(FORMAT)
    msg_length = len(massage)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(massage)
    re = client.recv(2048).decode(FORMAT)
    print(re)

msg = input('to start, type start. to disconnect press * ')
send(msg)
if msg == '*':
    send(DISCONNECT_MESSAGE)
elif msg == "start":
    current_time1 = time.localtime()
    print(current_time1)
    while True:
            re = client.recv(2048).decode(FORMAT)
            print(re)
            answer=input("type your answer: ")
            if answer == "*":
                send(DISCONNECT_MESSAGE)
            client.send(answer.encode())
            re = client.recv(2048).decode(FORMAT)
            print(re)
            current_time=time.localtime()
            current_time2=str(time.localtime())
            if current_time.tm_min==current_time1.tm_min + 1 and current_time.tm_sec == current_time1.tm_sec:
                client.send(current_time2.encode())
                print(current_time2)
                break
            else:
                pass
