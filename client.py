import socket

'''
enter ip address in the format
host(name):port
'''

ip_add = input('IP Address:')


def conn_server(ip_add=ip_add):
    host, port = ip_add.split(':')
    ADDR = (host, int(port))
    FORMAT = 'utf-8'

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(ADDR)

    print(f'[CONNECTED] Client connected to the server{ip_add}')

    msg = sock.recv(1024).decode(FORMAT)
    print(f'[server] {msg}')

    while True:
        msg = str(input('[YOU]>')).lower()

        sock.send(msg.encode(FORMAT))

        if msg == '':
            break

        else:
            msg = sock.recv(1024).decode(FORMAT)
            print(f'[server] {msg}')

    # recv_msg = sock.recv(1024)
    # sock.send(bytes('Received' ,'utf-8'))
    # print(recv_msg.decode('utf-8'))


if __name__=='__main__':
    conn_server()