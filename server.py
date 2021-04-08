import socket
import threading
import time
import random
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

dicte={
    "who i am?":" the server",
    "are you stupid?":"yes",
    "this is cool?":"yes",
    "are you pretty?":"no",
    "i am pretty?":"yes",
    "hiii":"hiii",
    "friends":"joey",
    "am i old?":"no",
    "are you old?":"yes",
    "this is fun?":"of course"
}
class question():
    def __init__(self):
        self.quest,self.answer =random.choice(list(dicte.items()))
        self.self=self.answer,self.quest
        dicte.pop(self.quest,self.answer)

q1 = question()
q2 = question()
q3 = question()
q4 = question()
q5 = question()
q6 = question()
q7 = question()
q8 = question()
q9 = question()
q10 = question()
question_list=[q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    welcome_msg = "Welcome to our game!!!"
    connected = True
    seccese = "you are right"
    fail = "you are wrong"
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                conn.send('Bye'.encode(FORMAT))
                conn.close()
                connected = False
            elif msg.lower() == 'start':
                game(conn, addr)
            else:
                conn.send("no function".encode(FORMAT))

            print(f"[{addr}] {msg}")

    conn.close()

def check(q ,player_answer):
    if q.answer==player_answer:
        massege="correct"
    else:
        massege="incorrect"

    return massege

def game(conn, addr):
    r_count, w_count = 0, 0
    current_time = time.localtime().tm_min
    print(current_time)
    conn.send("hello!!!".encode(FORMAT))
    for i in range(len(question_list)):
        time.sleep(0.5)
        ran = random.choice(question_list)
        question_list.remove(ran)
        conn.send(ran.quest.encode(FORMAT))
        player1_answer = conn.recv(1024).decode(FORMAT)
        massege = check(ran ,player1_answer)
        if massege == 'correct':
            r_count += 1
        else:
            w_count += 1
        conn.send(massege.encode(FORMAT))
        current_time1= str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec)
        print(current_time1, r_count, w_count)
        if current_time1 == current_time+1:
            timeing=conn.recv(1024).decode(FORMAT)
            print(timeing)
            break

def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CINECTION] {threading.activeCount() - 1}")
print('[STARTING] server is starting...')
start()
