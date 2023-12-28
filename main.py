import socket
import keyboard

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((socket.gethostbyname_ex(socket.gethostname())[-1][-1], 1234))

server.listen()

while True:
    user,adres = server.accept()

    while True:
        data = user.recv(1024).decode("utf-8").lower()

        if data == "okno":
            keyboard.press_and_release("alt + tab")