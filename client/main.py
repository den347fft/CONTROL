import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('192.168.0.101', 1234))

while True:
    try:
        x = input(">>")   
        client.send(x.encode("utf-8"))
    except ConnectionResetError:
        if x == "q":
            quit()
        print("Сервер пал")