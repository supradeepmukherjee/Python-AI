from threading import Thread
from time import sleep

def takeOrders():
    for i in range(1,4):
        print('taking order #',i)
        sleep(2)

def drink():
    for i in range(1,4):
        print('drinking cup#',i)
        sleep(3)

# creating threads
orderThread=Thread(target=takeOrders)
drinkThread=Thread(target=drink)

orderThread.start()
drinkThread.start()

# wait for both to finish
orderThread.join()
drinkThread.join()

print('done')