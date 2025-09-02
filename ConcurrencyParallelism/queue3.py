from multiprocessing import Process,Queue

def cook(q):
    q.put('cooked')

if __name__=='__main__':
    q=Queue()

    p=Process(target=cook,args=(q,))
    p.start()
    p.join()
    print(q.get())