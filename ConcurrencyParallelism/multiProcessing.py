from multiprocessing import Process
from time import sleep

def drink(name):
    print('tasting',name)
    sleep(3)
    print('drinking',name)

if __name__=='__main__':
    makers=[
        Process(target=drink,args=(f'Chai Maker #{i+1}',))
        for i in range(3)
    ]

    # start all process
    for p in makers:p.start()

    # wait for all to complete
    for p in makers:p.join()

    print('done')