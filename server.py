import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

class question():
    def __init__(self, quest, answer):
        self.quest=quest
        self.answer=answer

q1 = question('hi', 'hi').quest
q2 = question('bye', 'bye').quest
    
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
                conn.send("Msg received".encode(FORMAT))
                
            print(f"[{addr}] {msg}")
    
    conn.close()

def game(conn, addr):
    conn.send("hello!!! ".encode(FORMAT))

def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CINECTION] {threading.activeCount()-1}")


print('[STARTING] server is starting...')
start()
