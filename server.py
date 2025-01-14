import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.1.119',12345))
server.listen(7)
print('Server wait connection...')

clients = []

def connection():
    while True:
        con, addr = server.accept()
        login = con.recv(1024)
        print(f'{login.decode()} connection...')
        clients.append([con,addr,login])

def message():
    while True:
        for user in clients:
            message = user[0].recv(1024)
            if message:
                print(f'{user[2].decode()}: {message.decode()}')
                
th1 = threading.Thread(target=connection)
th2 = threading.Thread(target=message)
th1.start()
th2.start()
th1.join()
th2.join()