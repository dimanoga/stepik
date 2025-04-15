import asyncio

import aiohttp

status_codes = []


async def get_page(url, session, semaphore: asyncio.Semaphore):
    global status_codes
    async with semaphore:
        async with session.get(url) as response:
            status_code =  response.status
            status_codes.append(status_code)


async def main():
    semaphore = asyncio.Semaphore(10)
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            *[get_page(url=f'https://asyncio.ru/zadachi/5/{i}.html', semaphore=semaphore, session=session) for i in
              range(1, 1001)])
    print(sum(status_codes))


asyncio.run(main())
