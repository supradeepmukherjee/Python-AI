import asyncio,aiohttp

async def fetchUrl(session,url):
    async with session.get(url) as res:
        print(f'Fetched {url} with status {res.status}')

async def main():
    urls=['https://httpbin.org/delay/2']*3
    async with aiohttp.ClientSession() as session:
        tasks=[fetchUrl(session,url) for url in urls]
        await asyncio.gather(*tasks)

asyncio.run(main())