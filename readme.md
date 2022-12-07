In-order to get started with the Peer-to-Peer Network the following steps need to be taken


1. Step One
    Stsrt the server by running 
        python server.py 
    at the root directory(i.e that is the directory containing the server and peer file)
2. the server should give an output at the console with the following information
    [ SERVER_INFO ] Server started on host:port
        example:
            [ SERVER_INFO ] Server started on 192.168.1.11:9447

3. Copy the host:port pair from the server and make sure the server is still running:
    Example: you should copy the following data as it is:
        192.168.1.11:9447

4. Run peer.py file on a seperate terminal or tab in the same terminal:
    Example:
        python peer.py
    when running it should ask for the central server IP
5. When prompted for server IP paste the data from the server.py
    your terminal should look like this at the peer part after pasting the data:
        Example:
            Enter central  server ip:192.168.1.11:9447
    press enter  and wait until no more information is being displayed

6. Repeat this step as many times as possible for as many peers as you want

7. To close central server press ctrl+c and it will shut down but the peers will keeep their connection
