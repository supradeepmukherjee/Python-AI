import asyncio,time
from concurrent.futures import ProcessPoolExecutor

def encrypt(d):return d[::-1]

async def main():
    loop=asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        res=await loop.run_in_executor(pool,encrypt,'35bhu4iuy89uu8dusu8gh')
        print(res)

if __name__=='__main__': asyncio.run(main())