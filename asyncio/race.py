import threading

stock=0

def restock():
    global stock
    for _ in range(1000000):
        stock+=1

threads=[threading.Thread(target=restock) for _ in range(2)]

for t in threads:t.start()
for t in threads:t.join()

print(stock)