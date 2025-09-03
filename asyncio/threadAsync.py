import asyncio,time
from concurrent.futures import ThreadPoolExecutor

def checkStock(item):
    print('checking stock present/not of',item)
    time.sleep(2) # blocking operation as it blocks the main thread
    return f'stock of {item} available'

async def main():
    loop=asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        res=await loop.run_in_executor(pool,checkStock,'Atta')
        print(res)

asyncio.run(main())