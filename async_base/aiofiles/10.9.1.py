import asyncio
import os

semaphore = asyncio.BoundedSemaphore(1000)
dir = ''
total = 0


async def calc_nums(file_path):
    async with semaphore:
        with open(file_path, 'r') as f:
            number = int(f.readline())
            if number % 2 == 0:
                global total
                total += number


async def main():
    tasks = []
    for filename in os.listdir(dir):
        tasks.append(calc_nums(os.path.join(dir, filename)))
    await asyncio.gather(*tasks)
    print(f'Total: {total}')


asyncio.run(main())
