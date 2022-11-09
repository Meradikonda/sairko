'''
    simple HTTP/1. Server
'''

import socket
from _thread import *


def ip_addr():
    port = 5050
    ip = socket.gethostbyname(socket.gethostname())

    server = f'{ip}:{port}'

    return server


def threaded(conn):

    # Get the client request and filename passed by the user
    request = conn.recv(1024).decode().split('\n')[0]

    filename = request.split()[1]
       
    try:
        
        fin = open(f'http_sockets/markup{filename}')
        content = fin.read()
        fin.close()

        response = 'HTTP/1.1 200 0K\n\n' + content

    except (FileNotFoundError, IsADirectoryError, IndexError):        
        response = 'HTTP/1.1 200 0K\n\n 404 Not Found'


    # send HTTP response        
    conn.sendall(response.encode())
    conn.close()


def start_server(ip_addr=ip_addr()):
    '''
    host = socket.gethostbyname(socket.gethostname())
    port = 8000
    '''

    host, port = ip_addr.split(':')
    addr = (host, int(port))

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # server.bind((host, port))
    server.bind(addr)
    server.listen(1)

    print(f'[SERVER] {host} is running on port {port}')
    # print(f'Listening on port: {port}')
    print(f'Address is {host}:{port}')

    while True:
        try:
            # wait for client connections
            conn, addr = server.accept()    
            
            start_new_thread(threaded, (conn,)) 
        except KeyboardInterrupt:
            print("[SERVER] Closing... BYE")
            break;
       
    server.close()

if __name__=='__main__':
    start_server()