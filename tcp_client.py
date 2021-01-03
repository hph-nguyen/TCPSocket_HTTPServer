import socket

with socket.socket() as s:
    host = socket.gethostname()
    port = 12345
    s.connect((host,port))

    while True:
        val = input("Please enter a String (Enter: 'stop' to end process) : ")
        s.send(val.encode('utf-8'))
        if val == 'stop':
            break
        byte = s.recv(1024)
        print(byte.decode('utf-8'))