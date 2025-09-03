import asyncio,threading,time

def worker():
    while True:
        time.sleep(1)
        print('system health:')

async def getOrders():
    await asyncio.sleep(3)
    print('Orders fetched')

threading.Thread(target=worker,daemon=True).start()

asyncio.run(getOrders())