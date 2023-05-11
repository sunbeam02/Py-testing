import socket

#host = socket.gethostbyname(socket.gethostname())
host = "192.168.10.67"
port = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((host, port))
    client.settimeout(60)
  

    while True:
        response = client.recv(1024)
        print(response.decode())
        message = input("Chat (Client): ")
        client.send(message.encode())
       
       