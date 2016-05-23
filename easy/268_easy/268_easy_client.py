#
# /r/dailyprogrammer Challenge #268 [Easy] 
# Network and Cards: Part 1, The network
#                        
# https://www.reddit.com/r/dailyprogrammer/comments/4knivr/20160523_challenge_268_easy_network_and_cards/
# 

# This is the CLIENT PORTION of the Client-Server network of this problem

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