import asyncio
import os

import aiofiles
from aiocsv import AsyncDictReader

semaphore = asyncio.BoundedSemaphore(1000)
dir = ''
total = 0


async def calc_nums(file_path):
    global total
    async with semaphore:
        async with aiofiles.open(file_path, 'r') as f:
            async for row in AsyncDictReader(f,fieldnames=['num']):
                total += int(row['num'])


async def main():
    tasks = []
    for filename in os.listdir(dir):
        tasks.append(calc_nums(os.path.join(dir, filename)))
    await asyncio.gather(*tasks)
    print(f'Total: {total}')


asyncio.run(main())
