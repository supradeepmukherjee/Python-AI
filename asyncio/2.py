import asyncio
from time import time,sleep

async def cook(n):
    print('cooking ',n)
    await asyncio.sleep(2)
    # sleep(2)
    print(n,' ready')

async def main():
    await asyncio.gather(cook('rice'),cook('roti'),cook('veg'))

start=time()
asyncio.run(main())
end=time()

print(f'{start},{end},{end-start}sec')