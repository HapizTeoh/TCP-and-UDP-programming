import socket,_thread,random,datetime

UDP_IP_ADDRESS = input(str("Enter server IP: "))
host = "192.168.0.177"
port = random.randint(1,5000)
UDP_PORT_NO = 9876
clientSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
clientSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

currenTime = datetime.datetime.now()
formatted = (currenTime.strftime("%I:%M:%S %p"))


print("Sending to server: "+UDP_IP_ADDRESS)
clientSock.bind((host, random.randint(1,5000)))


def listening_thread():
    saved = []
    while True:
        data = clientSock.recvfrom(1024)
        if data[0].decode() not in saved and data[0].decode()!=" ":
            print("\n\n"+formatted, "Received message: ", data[0].decode())
            saved.append(data[0].decode())

_thread.start_new_thread(listening_thread,())

while True:

    Message = input(str(str(currenTime.strftime("%I:%M:%S %p"))+" Client: "))
    clientSock.sendto(Message.encode(),(UDP_IP_ADDRESS,UDP_PORT_NO))

