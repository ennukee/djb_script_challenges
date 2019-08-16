#
# /r/dailyprogrammer Challenge #268 [Easy] 
# Network and Cards: Part 1, The network
#                        
# https://www.reddit.com/r/dailyprogrammer/comments/4knivr/20160523_challenge_268_easy_network_and_cards/
# 

# This is the SERVER PORTION of the Client-Server network of this problem

import socket
import sys
import random
from _thread import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
users = {'root': 'root'} # server

try:
  s.bind(('localhost', 8888))
except socket.error as msg:
  print('Bind failed. Is port 8888 currenttly in use?')
  sys.exit()
 
s.listen(10)
 
def cthread(conn):
  username = "root"

  while username in users.values():
    username = 'user{}'.format(random.randrange(100000))
  users[conn] = username

  conn.send('Welcome to the server, {}. Type something and hit enter\n'.format(username).encode('utf-8'))
  
  try:
    while 1:
      data = conn.recv(1024)
      if not data: 
        break

      data = str(data, 'utf-8')
      prefix = data[0:3]

      if prefix == 'usr':
        if data[4:8] == 'set ':

          if len(data[8:]) > 12:
            conn.sendall('Your desired username is too long (max 12 characters)'.encode('utf-8'))

          else:
            old, new = users[conn], data[8:]
            if new in users:
              conn.sendall('Your username has already been taken.'.encode('utf-8'))
            else:
              conn.sendall('Your username has been set to {}'.format(new).encode('utf-8'))
              users[conn] = new

        elif data[4:8] == 'list':
          online = '\n'.join([user for user in users.values() if user != 'root'])
          conn.sendall('Users currently online:\n{}'.format(online).encode('utf-8'))
        else:
          conn.sendall('Your username is {}'.format(users[conn]).encode('utf-8'))
      else:
        conn.sendall(data.encode('utf-8'))
  except Exception as e:
    print('Error detected!')
    print('{}: {}'.format(type(e).__name__, e))
  finally:
    users.pop(conn, None)
    conn.close()
    print('Client on ' + addr[0] + ':' + str(addr[1]) + ' has been disconnected')
 
while 1:
  conn, addr = s.accept()
  print('Connected with ' + addr[0] + ':' + str(addr[1]))

  start_new_thread(cthread, (conn,))

s.close()