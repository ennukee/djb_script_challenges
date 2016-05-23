import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8888))

data = s.recv(1024)
print(str(data, 'utf-8')) # Welcome message

try:
  while 1:
    message = input('> ')
    s.sendall(message.encode('utf-8'))

    data = s.recv(1024)
    print('Received: {}'.format(str(data, 'utf-8')))
finally:
  s.close()