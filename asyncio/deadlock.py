import threading

lockA=threading.Lock()
lockB=threading.Lock()

def task1():
    with lockA:
        print('task1 acquired lock a')
        with lockB:
            print('task1 acquired lock b')

def task2():
    with lockB:
        print('task2 acquired lock a')
        with lockA:
            print('task2 acquired lock b')

thread1=threading.Thread(target=task1)
thread2=threading.Thread(target=task2)

thread1.start()
thread2.start()