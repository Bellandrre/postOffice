'''
A simple socket program to demostrate communication
Between client and server using UDP sockets. 

Servers sends back a capitalized version of the String
@Karthik Kolathumani
'''
import socket

MAX_SIZE_BYTES = 65535

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # AFT_NET Family for IPv4 addresses.
                                                          # AF_INET6 family for IPv6.
                                                          # AF_UNIX Unix Domain Sockets. A POXIS compliant socket which is used for interPROCESS communication. 
                                                                                        # INET vs Unix sockets - Unix sockets are bound to a file while INET sockets
                                                                                        # are bound to an IP address. So INET sockets can be also used by remote machines.   

                                                          #SOCK_DGRAM represents the datagrams (chunks) for UDP.
                                                          #SOCK_STREAM represents the datagrams for TCP.
    port = 3000
    hostname = '127.0.0.1'
    s.bind((hostname, port))                                         
    print('Started Listening at {}'.format(s.getsockname())) 

    # Listen infinitely
    while True:
        data, clientAddress = s.recvfrom(MAX_SIZE_BYTES) # Receive at most 65535 bytes at once
        message = data.decode('ascii')
        capitalized = message.upper()
        message = 'The client at {} say {!r}'.format(clientAddress, message)
        print(message)
        data = capitalized.encode('ascii')
        s.sendto(data, clientAddress)
