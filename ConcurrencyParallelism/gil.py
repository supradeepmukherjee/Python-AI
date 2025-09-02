# Global Interpreter Lock

import threading,time

def drink():
    print(f'{threading.current_thread().name} started drinking')
    count=0
    for _ in range(100_000_000):count+=1
    print(f'{threading.current_thread().name} finished drinking')

thread1=threading.Thread(target=drink,name='t1')
thread2=threading.Thread(target=drink,name='t2')

start=time.time()
thread1.start()
thread2.start()
thread2.join()
thread1.join()
end=time.time()
print(f'{start},{end},{end-start:.2f}')