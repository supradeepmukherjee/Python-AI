import threading,time

def prepare(type_,wait):
    print(type_,'preparing')
    time.sleep(wait)
    print(type_,'ready')

t1=threading.Thread(target=prepare, args=('Bhaat',5))
t2=threading.Thread(target=prepare, args=('Roti',4))

t1.start()
t2.start()
t1.join()
t2.join()