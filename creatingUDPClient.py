import socket

MAX_SIZE_BYTES = 65535

def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    inputMessage = input('Input lowercase sentence: ')
    data = inputMessage.encode('ascii')
    s.sendto(data, ('127.0.0.1', 3000))
    logMessage = 'The OS assigned the ephemeral port {} to me'.format(s.getsockname())
    print(logMessage)
    data, address = s.recvfrom(MAX_SIZE_BYTES) ## Receive from the server
    serverText = data.decode('ascii')
    print('The server {} replied with {!r}'.format(address, serverText))

