import asyncio
import os

import aiofiles
from aiocsv import AsyncDictReader

semaphore = asyncio.BoundedSemaphore(1000)
total = 0


async def calc_nums(file_path):
    global total
    async with semaphore:
        async with aiofiles.open(file_path, 'r') as f:
            async for row in AsyncDictReader(f, fieldnames=['num']):
                total += int(row['num'])


def list_directory_contents(path):
    res = []
    # сканируется вся директория path, включая корневую директорию, все подпапки и файлы
    for root, dirs, files in os.walk(path):
        if files:
            # полный путь к файлу
            path_file = os.path.join(root, *files)
            # print(path_file)
            res.append(path_file)
    return res


async def main():
    paths = list_directory_contents('')
    await asyncio.gather(*[calc_nums(path) for path in paths])
    print(f'Total: {total}')


asyncio.run(main())
