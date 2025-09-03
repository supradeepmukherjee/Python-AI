import asyncio

async def drink():
    print('Drinking')
    await asyncio.sleep(2)
    print('done')

asyncio.run(drink())