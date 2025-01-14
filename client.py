import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('192.168.1.119',12345))
print('Server connect...')
login = 'Dragonborn'
client.sendall(login.encode())
while True:
    data = input('message: ')
    client.sendall(data.encode())

#data = input('message: ')
#client.sendall(data.encode())
#client.close()