import socket
import keyboard
import pyttsx3
import webbrowser
engine = pyttsx3.Engine()
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((socket.gethostbyname_ex(socket.gethostname())[-1][-1], 1234))

server.listen()

while True:
    user,adres = server.accept()
    if user:
        print("Подключено устройство")
    try:
        while True:
            data = user.recv(1024).decode("utf-8").lower()
            if "say" in data:
                engine.say(data[3:])
                engine.runAndWait()
            if "press" in data:
                try:
                    keyboard.press_and_release(data[6:])
                except Exception:
                    pass
            if "eve" in data:
                 try:
                    eval(data[4:])
                 except Exception:
                    pass
            if "browser" in data:
                 webbrowser.open_new_tab(data[8:])
    except Exception:
                    pass