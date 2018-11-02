import selectors
from socket import *

def accept(sk,mask):
    conn,addr=sk.accept()
    sel.register(conn,selectors.EVENT_READ,read)

def read(conn,mask):
    try:
        data=conn.recv(1024)
        if not data:
            print('closing',conn)
            sel.unregister(conn)
            conn.close()
            return
        conn.send(data.upper()+b'_SB')
    except Exception:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()

sk=socket()
sk.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sk.bind(('127.0.0.1',8088))
sk.listen(5)
sk.setblocking(False) #设置socket的接口为非阻塞
sel=selectors.DefaultSelector()   # 选择一个适合我的IO多路复用的机制
sel.register(sk,selectors.EVENT_READ,accept)
#相当于网select的读列表里append了一个sk对象,并且绑定了一个回调函数accept
# 说白了就是 如果有人请求连接sk,就调用accrpt方法

while True:
    events=sel.select() #检测所有的sk,conn，是否有完成wait data阶段
    for sel_obj,mask in events:  # [conn]
        callback=sel_obj.data #callback=read
        callback(sel_obj.fileobj,mask) #read(conn,1)