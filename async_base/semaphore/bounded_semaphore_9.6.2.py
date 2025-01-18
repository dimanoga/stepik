import asyncio

free_semaphore = asyncio.Semaphore(2)
premium_semaphore = asyncio.Semaphore(10)


async def convert_file(file_name: str, semaphore: asyncio.Semaphore):
    async with semaphore:
        await asyncio.sleep(1)
        print(f'Файл {file_name} обработан')


async def main():
    files = map(str, input().split())
    plan = input()
    if plan == 'free':
        semaphore = free_semaphore
    else:
        semaphore = premium_semaphore
    await asyncio.gather(*[convert_file(file, semaphore) for file in files])


asyncio.run(main())
