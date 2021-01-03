import socket

with socket.socket() as s:
    host = socket.gethostname()             # return hostname
    port = 12345
    s.bind((host,port))                     # mit Socket verbinden
    s.listen()                              # als Überwachungszustand setzen --> als Server setzen.

    while True:
        connection, addr = s.accept()       # Tupel-typ: (socket, any)
        with connection:
            print('Informationen des Sockets:', connection, '\nVerbindung mit ',addr)
            while True:
                bytes = connection.recv(1024)   # 1024 = buffersize
                msg = bytes.decode('utf-8')     # dekodiert Binär-string nach UTF-8-Format
                msg = msg.upper()
                if msg == 'STOP':
                    break
                connection.send(msg.encode('utf-8'))
            print('Verbindung beendet')

# Benutzung von with socket.socket() as s --> socket.close() muss nicht geschrieben werden, Code-Block schließt sich automatisch.