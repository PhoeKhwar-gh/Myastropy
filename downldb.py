import aiohttp
import asyncio
import os

async def download_file(session, url, dest):
    async with session.get(url) as resp:
        if resp.status == 200:
            with open(dest, 'wb') as f:
                f.write(await resp.read())

async def main():
    urls = [
        f"https://www.dropbox.com/scl/fo/y3naz62gy6f6qfrhquu7u/h/all_ast?rlkey=ejltdhb262zglm7eo6yfj2940&dl=0"
        for n in range(13000, 14000)  # Example range
    ]
    os.makedirs("ephe", exist_ok=True)
    async with aiohttp.ClientSession() as session:
        tasks = [
            download_file(session, url, f"ephe/se{n}s.se1")
            for n, url in zip(range(13000, 14000), urls)
        ]
        await asyncio.gather(*tasks)

asyncio.run(main())