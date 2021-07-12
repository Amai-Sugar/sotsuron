import socket
import time
import datetime

target_host="192.168.1.20"
target_port=1234
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))
while True:
    time.sleep(1800)
    data = str(datetime.datetime.now()) + "\n"
    client.send(data.encode('utf-8'))

