import socket
import pickle
import json

PORT = 9910
ADDRESS = socket.gethostname()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((ADDRESS,PORT))

def receive():
    full_msg = ''
    while True:
        msg = client.recv(1024)
        if len(msg) <= 0:
            break
        full_msg += msg.decode('utf-8')
        print(full_msg)
        return full_msg
        break

name = input("Enter your name: ")
client.send(bytes(name, 'utf-8'))
receive()

msg =''
while msg!= 'PROGRAM END':

    menu = input("Enter your input: ")
    client.send(bytes(menu, 'utf-8'))
    msg = receive()







