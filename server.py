import socket
import pickle
import json

PORT = 9910
ADDRESS = socket.gethostname()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created!')
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind((ADDRESS,PORT))

server.listen(3)
print("Waiting for connections...")

booknum = 0
bookcode = []
flight = {}
path = {'100':"Singapore to Cambodia",'200':"Singapore to Japan",'300':"Singapore to Indonesia",
        '400':"Malaysia to Cambodia",'500':"Malaysia to Japan",'600':"Malaysia to Indonesia",
        '700':"Thailand to Cambodia",'800':"Thailand to Japan",'900':"Thailand to Indonesia"}
while True:
    c, addr = server.accept()
    name = c.recv(1024).decode()
    print('Connected with', addr,name)


    priceSinga = {1: 100, 2: 200, 3: 300}
    priceMas = {1: 400, 2: 500, 3: 600}
    priceThai = {1: 700, 2: 800, 3: 900}
    originCountries = {1: priceSinga, 2: priceMas, 3: priceThai}

    while True:
        c.send(bytes('\nYou are connected! Welcome '+name+ '\nChoose any of the below \n1.Book a flight \n2.View flight \n3.Cancel flight \n4.Exit', 'utf-8'))
        Menu = c.recv(1024).decode()
        if int(Menu) == 1:
            c.send(bytes('You have choose to book a flight', 'utf-8'))
            c.send(bytes('\nSelect origin: \n1.Singapore \n2.Malaysia \n3.Thailand', 'utf-8'))
            Menu = c.recv(1024).decode()
            Origin = int(Menu)
            c.send(bytes('Select destination: \n1.Cambodia \n2.Japan \n3.Indonesia', 'utf-8'))
            Menu = c.recv(1024).decode()
            Destination = int(Menu)
            Totalprice = originCountries[Origin][Destination]
            booknum+=1
            bookcode.append('A00'+str(booknum))
            flight.update({bookcode[booknum-1]:str(Totalprice)})
            c.send(bytes('Your flight total price is RM' + str(Totalprice) + '\nYour bookcode is '+bookcode[booknum-1], 'utf-8'))
            c.send(bytes('\nContinue?(y/n)', 'utf-8'))
            Menu = c.recv(1024).decode()
            if Menu == 'n'.casefold():
                c.send(bytes("PROGRAM END", 'utf-8'))
                c.close()

        elif int(Menu)==2:
            c.send(bytes('Enter your bookcode', 'utf-8'))
            Menu = c.recv(1024).decode()
            if Menu not in bookcode:
                c.send(bytes('Bookcode not found!', 'utf-8'))
                Menu == 'y'
            else:
                c.send(bytes("Your book code is: "+Menu+"\nFlight from "+path[flight[Menu]]+" with the price of RM"+ (flight[Menu]), 'utf-8'))
                c.send(bytes('\nContinue?(y/n)', 'utf-8'))
                Menu = c.recv(1024).decode()
                if Menu == 'n'.casefold():
                    c.send(bytes("PROGRAM END", 'utf-8'))
                    c.close()

        elif int(Menu)==3:
            c.send(bytes('Enter your bookcode', 'utf-8'))
            Menu = c.recv(1024).decode()
            del flight[Menu]
            bookcode.remove(Menu)
            c.send(bytes('Flight cancelled!', 'utf-8'))
            c.send(bytes('\nContinue?(y/n)', 'utf-8'))
            Menu = c.recv(1024).decode()
            if Menu == 'n'.casefold():
                c.send(bytes("PROGRAM END", 'utf-8'))
                c.close()


        elif int(Menu)==4:
            c.send(bytes("PROGRAM END", 'utf-8'))
            c.close()





