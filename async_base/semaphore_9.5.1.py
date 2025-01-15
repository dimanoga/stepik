import asyncio

semaphore = asyncio.Semaphore(3)

total = 0
async def do_smth(user):
    global total
    async with semaphore:
        total += 1
        print(f'Пользователь {user} делает запрос')
        await asyncio.sleep(1)
        print(f'Запрос от пользователя {user} завершен')
        print(f'Всего запросов: {total}')


async def main():
    users = ["sasha", "petya", "masha", "katya", "dima", "olya", "igor", "sveta", "nikita", "lena",
             "vova", "yana", "kolya", "anya", "roma", "nastya", "artem", "vera", "misha", "liza"]
    await asyncio.gather(*[do_smth(user) for user in users])


asyncio.run(main())
