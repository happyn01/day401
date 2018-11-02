# 进程 启动多个进程 进程之间是由操作系统负责调用
# 线程 启动多个线程 真正被CPU执行的最小单位实际是线程
    # 开启一个线程 创建一个线程 寄存器 堆栈
    # 关闭一个线程
# 协程
    # 本质上是一个线程
    # 能够在多个任务之间切换来节省一些IO时间
    # 协程中任务之间的切换也消耗时间,但是开销要远远小于进程线程之间的切换
# 实现并发的手段
# import time
# def consumer():
#     while True:
#         x = yield
#         time.sleep(1)
#         print('处理了数据 :',x)
#
# def producer():
#     c = consumer()
#     next(c)
#     for i in range(10):
#         time.sleep(1)
#         print('生产了数据 :',i)
#         c.send(i)
#
# producer()

# 真正的协程模块就是使用greenlet完成的切换
from greenlet import greenlet
def eat():
    print('eating start')
    g2.switch()
    print('eating end')
    g2.switch()

def play():
    print('playing start')
    g1.switch()
    print('playing end')
g1 = greenlet(eat)
g2 = greenlet(play)
g1.switch()
from gevent import monkey;monkey.patch_all()
# import time
# import gevent
# import threading
# def eat():
#     print(threading.current_thread().getName())
#     print(threading.current_thread())
#     print('eating start')
#     time.sleep(1)
#     print('eating end')
#
# def play():
#     print(threading.current_thread().getName())
#     print(threading.current_thread())
#     print('playing start')
#     time.sleep(1)
#     print('playing end')
#
# g1 = gevent.spawn(eat)
# g2 = gevent.spawn(play)
# g1.join()
# g2.join()

# 进程和线程的任务切换右操作系统完成
# 协程任务之间的切换由程序(代码)完成,只有遇到协程模块能识别的IO操作的时候,程序才会进行任务切换,实现并发的效果

# 同步 和 异步
# from gevent import monkey;monkey.patch_all()
# import time
# import gevent
#
# def task(n):
#     time.sleep(1)
#     print(n)
#
# def sync():
#     for i in range(10):
#         task(i)
#
# def async():
#     g_lst = []
#     for i in range(10):
#         g = gevent.spawn(task,i)
#         g_lst.append(g)
#     gevent.joinall(g_lst)  # for g in g_lst:g.join()

# sync()
# async()


# 协程 : 能够在一个线程中实现并发效果的概念
    #    能够规避一些任务中的IO操作
    #    在任务的执行过程中,检测到IO就切换到其他任务

# 多线程 被弱化了
# 协程 在一个线程上 提高CPU 的利用率
# 协程相比于多线程的优势 切换的效率更快

# 爬虫的例子
# 请求过程中的IO等待
# from gevent import monkey;monkey.patch_all()
# import gevent
# from urllib.request import urlopen    # 内置的模块
# def get_url(url):
#     response = urlopen(url)
#     content = response.read().decode('utf-8')
#     return len(content)
#
# g1 = gevent.spawn(get_url,'http://www.baidu.com')
# g2 = gevent.spawn(get_url,'http://www.sogou.com')
# g3 = gevent.spawn(get_url,'http://www.taobao.com')
# g4 = gevent.spawn(get_url,'http://www.hao123.com')
# g5 = gevent.spawn(get_url,'http://www.cnblogs.com')
# gevent.joinall([g1,g2,g3,g4,g5])
# print(g1.value)
# print(g2.value)
# print(g3.value)
# print(g4.value)
# print(g5.value)

# ret = get_url('http://www.baidu.com')
# print(ret)

# socket server









