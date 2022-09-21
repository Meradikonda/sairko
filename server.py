import socket
import threading
from datetime import datetime
from tzlocal import get_localzone
from pytz import timezone


def ip_addr():
    port = 5050
    ip = socket.gethostbyname(socket.gethostname())

    server = f'{ip}:{port}'

    return server


def get_time():
    format = "%a %b %d %H:%M:%S %Z %Y"

    # current UTC time
    now_utc = datetime.now(timezone('UTC'))

    # convert to local time
    now_local = now_utc.astimezone(get_localzone())

    return now_local.strftime(format)

def handle_client(conn, addr):

    '''
        No defined way to handle incoming messages after the second 'time' is send.
        there can be 2 approaces to handle this inorder to avoid breaking the system:
            1. Return the received message back to the client or 
            2. Print the received message.
        
        NOTE: This are not important they are just used for the purposes of bug prevention AND system 
        failure(or hanging)
    '''
    TIME = 0
    size = 1024
    global FORMAT  
    FORMAT = 'utf-8'

    print(f'[NEW CONNE] {addr} connected')

    mess =  f'Hello client #{threading.active_count() -1}'
    conn.send(mess.encode(FORMAT))    
    print(mess)
    # run infinitely listening at the clients
    while True:
        message = conn.recv(size).decode(FORMAT)        

        if message == '':
            break

        elif message=='time' and TIME==0:
            time = get_time()
            conn.send(f'TIME:{TIME} \n got_timed:{time}'.encode(FORMAT))
            TIME += 1            

        elif message=='time' and TIME==1:
            time = get_time().upper()
            conn.send(f'TIME:{TIME} \n got_timed:{time}'.encode(FORMAT))
            TIME += 1
       
        else:
            conn.send(f'Received "{message}" as the message'.encode(FORMAT))
            TIME += 1
       


        print(f"[{addr}] {message}")

        
    conn.close()

def start_server(ip_addr=ip_addr()):
    
    host, port = ip_addr.split(':')
    addr = (host, int(port))

    print("[STARTING] Server is starting...")

    # init/setup our server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(addr)
    server.listen()
    
    print(f'[LISTENING] Server running on: {ip_addr}')
    
    # run server infinetly
    while True:
        conn, clientAddr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, clientAddr))
        thread.start()


if __name__=='__main__':
    start_server()
