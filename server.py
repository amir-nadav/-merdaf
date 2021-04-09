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
MONEY=5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

esaydict={
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
hardict={
   "what is israel?":"a country",
    "what is god":"evrything",
    "when did world war 2 started?":"1940",
    "what is A":"a letter",
}
class question():
    def __init__(self):
        self.quest,self.answer =random.choice(list(esaydict.items()))
        self.self=self.answer,self.quest
        esaydict.pop(self.quest,self.answer)
class hardquestion():
    def __init__(self):
        self.question,self.answer=random.choice(list(hardict.items()))
        self.self=self.answer,self.question
        hardict.pop(self.answer,self.question)
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
qu1=hardquestion()
qu2=hardquestion()
qu3=hardquestion()
qu4=hardquestion()
hardquest=[qu1,qu2,qu3,qu4]
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
    r_hardcount,w_hardcount=0,0
    current_time = time.localtime().tm_min
    current_time3=time.localtime().tm_sec
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
        current_time1=time.localtime().tm_min
        current_time2=time.localtime().tm_sec
        print( r_count, w_count)
        if current_time1==current_time+1:
            amount=str(r_count*MONEY)
            time.sleep(0.3)
            conn.send(amount.encode())
            print("the player got:",amount,"₪")
            break
    howmuch = conn.recv(1024).decode()
    howmuch = int(howmuch)
    for i in range(howmuch):
        ran1 = random.choice(hardquest)
        conn.send(ran1.question.encode(FORMAT))
        hardquest.remove(ran1)
        player1_hardanswer = conn.recv(1024).decode(FORMAT)
        messege = check(ran1, player1_hardanswer)
        if messege == 'correct':
            r_hardcount += 1
        else:
            w_hardcount += 1
    total=r_hardcount * MONEY
    string="you erend in this round:",total
    string=str(string)
    conn.send(string.encode())
    print("he erend in this round:",total, "₪")



def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        thread_list=[]
        thread_list.append(thread)
        print(f"[ACTIVE CINECTION] {threading.activeCount() - 1}")
print('[STARTING] server is starting...')
start()
