import select
import socket

sk = socket.socket()
sk.bind(('127.0.0.1',8000))
sk.setblocking(False)
sk.listen()

read_lst = [sk]
while True:   # [sk,conn]
    r_lst,w_lst,x_lst = select.select(read_lst,[],[])
    for i in r_lst:
        if i is sk:
            conn,addr = i.accept()
            read_lst.append(conn)
        else:
            ret = i.recv(1024)
            if ret == b'':
                i.close()
                read_lst.remove(i)
                continue
            print(ret)
            i.send(b'goodbye!')