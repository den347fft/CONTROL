import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('192.168.0.101', 1234))

while True:
    try:
        x = input(">>")
        if x == "q":
            quit()
        elif x == "press":
            print("input button or buttons with +")
        elif x == "browser":
            print("input url")
        client.send(x.encode("utf-8"))
    except ConnectionResetError:
        if x == "q":
            quit()
        print("Сервер пал")