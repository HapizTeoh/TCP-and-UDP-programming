import time,_thread,sys,socket

clientlist= []
msglist = {}

UDP_IP_ADDRESS = "0.0.0.0"
UDP_PORT_NO = 9876
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

def noisy_thread():
    while True:


        data = serverSock.recvfrom(1024)
        print(data[1])
        if data[1] not in clientlist:
            clientlist.append(data[1])
            position = (clientlist.index(data[1]))
            msglist[position] = data[0].decode()
        else:
            position = (clientlist.index(data[1]))
            msglist.setdefault(str(position),[]).append(data[0].decode())

        print("\nReceived message:", data[0].decode() + " from " + str(data[1]))




_thread.start_new_thread(noisy_thread,())

while True :
    print ("Currently "+str(len(clientlist))+" client(s) connected")
    time.sleep(2)
    o=0
    for i in clientlist:

        print("Client "+str(o)+" is sending from " +i[0]+" through port "+str(i[1]))
        o+=1
        secon = str(clientlist.index(i))
        Message = msglist[clientlist.index(i)]
        unwanted = []
        unwanted.append(i)
        for x in clientlist:
            if x not in unwanted:
                serverSock.sendto(Message.encode(), x)
                msglist[clientlist.index(i)] = ""
                if secon in msglist:
                    u = 0
                    while u < len(msglist[secon]):
                        Message = msglist[secon][u]
                        serverSock.sendto(Message.encode(), x)
                        u += 1



