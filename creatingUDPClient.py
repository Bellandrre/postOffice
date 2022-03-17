import socket

MAX_SIZE_BYTES = 65535
HOST = '127.0.0.1'
PORT = '3000'

def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

    s.connect((HOST, PORT)) # connect to make sure the client does not receive data from other servers

    inputMessage = input('Input lowercase sentence: ')
    data = inputMessage.encode('ascii')

    logMessage = 'The OS assigned the ephemeral port {} to me'.format(s.getsockname())
    print(logMessage)

    s.send(data)

    data, address = s.recv(MAX_SIZE_BYTES) ## Receive from the server
    serverText = data.decode('ascii')

    print('The server {} replied with {!r}'.format(address, serverText))

