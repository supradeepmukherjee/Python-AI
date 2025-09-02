import threading,time

def cpuHeavy():
    print(f'Crunching some nummbers')
    total=0
    for i in range(10**7):
        total+=i
    print('done',total)

start=time.time()
threads=[threading.Thread(target=cpuHeavy) for _ in range(2)]
[t.start() for t in threads]
[t.join() for t in threads]
print(f'{time.time()-start:.2f}sec')