import socket
import sys
s = socket.socket()
s.bind(("localhost",9999))
s.listen(10) # Acepta hasta 10 conexiones entrantes.

i = 1
while True:
    sc, address = s.accept()

    print address
    f = open('file_'+ str(i)+".wav",'wb') #open in binary
    i=i+1
    while (True):
        # recibimos y escribimos en el fichero
        l = sc.recv(1024)
        f.write(l)

        if not l:
            break

    f.close()
    sc.close()
    print('copied the file.')

s.close()
