import socket
import time
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
MOUNY=5000
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
    current_time=time.localtime().tm_sec
    current_time2= time.localtime().tm_min
    print(current_time2)
    while True:
            re = client.recv(2048).decode(FORMAT)
            print(re)
            answer=input("type your answer: ")
            if answer == "*":
                send(DISCONNECT_MESSAGE)
            client.send(answer.encode())
            current_time3=time.localtime().tm_min
            current_time1=time.localtime().tm_sec
            re = client.recv(2048).decode(FORMAT)
            print(re)
            if current_time3==current_time2+1:
                time.sleep(0.3)
                send1=client.recv(2048).decode(FORMAT)
                print("you've erned:",send1,"₪")
                break
    round = input("how much mony you would like? 1-5000,2-7000,3-0000")
    round = str(round)
    client.send(round.encode())
    round=int(round)
    for i in range(round):
        print(client.recv(1024).decode())
        answerhard = input("enter your enswer: ")
        client.send(answerhard.encode())
    print(client.recv(1024).decode())


