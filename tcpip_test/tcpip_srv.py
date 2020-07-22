import socket
import sys

from CONST_DEFINE import SRV_ADDR, SRV_PORT, BUFFER_SIZE

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (SRV_ADDR, SRV_PORT)
# print >>sys.stderr, 'starting up on %s port %s' % server_address
print('starting up on %s port %s' % server_address)

sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

conn, addr = sock.accept()
# print('connection address:%s' % addr)
print(addr)

while True:
  data = conn.recv(BUFFER_SIZE)
  if not data: break
  print('received data:%s' % data)
  conn.send(data)
conn.close()

# while True:
#   # Wait for a connection
#   # print >>sys.stderr, 'waiting for a connection' 
#   print('waiting for a connection')
#   connection, client_address = sock.accept()
#   print(connection, client_address)
# 
# try:
#   print >>sys.stderr, 'connection from', client_address
#   # Receive the data in small chunks and retransmit it
#   while True:
#     data = connection.recv(16)
#     print >>sys.stderr, 'received "%s"' % data
#     if data:
#      print >>sys.stderr, 'sending data back to the client'
#      connection.sendall(data)
#     else:
#       print >>sys.stderr, 'no more data from', client_address
#       break
# finally:
#   # Clean up the connection
#   connection.close()


