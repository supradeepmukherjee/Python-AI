import threading,time

def boil():
    print('Boiling')
    time.sleep(2)
    print('Boiled')

def fry():
    print('Frying')
    time.sleep(3)
    print('Fried')

start=time.time()

t1=threading.Thread(target=boil)
t2=threading.Thread(target=fry)

t1.start()
t2.start()
t1.join()
t2.join()

end=time.time()
print(f'{start},{end},{end-start:.2f}')