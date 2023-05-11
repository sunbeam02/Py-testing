
import socket

host = socket.gethostbyname(socket.gethostname())
print(host) #to check my ipaddress
port = 8000


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((host,port))
    server.listen()
    print('Listening for connection')

    while True:
        
        print("waiting for client to connect")
        client, address = server.accept()
        print(f"{address[0]} has connected to port {address[1]}")
        message = 'hi'


        client.send(message.encode())
        while True:
            response = client.recv(1024)
            print(response)
            if response == 'quit':
                break
            message = input('Chat (Server): ')
            client.send(message.encode())

