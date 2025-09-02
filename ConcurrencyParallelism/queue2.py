import multiprocessing,time

def cpuHeavy():
    print(f'Crunching some nummbers')
    total=0
    for i in range(10**7):
        total+=i
    print('done',total)

if __name__=='__main__':
    start=time.time()
    processes=[multiprocessing.Process(target=cpuHeavy) for _ in range(2)]
    [t.start() for t in processes]
    [t.join() for t in processes]
    print(f'{time.time()-start:.2f}sec')