import asyncio


async def connect_to_db(user: str, condition) -> None:
    print(f'Пользователь {user} ожидает доступа к базе данных')
    async with condition:
        await asyncio.sleep(.1)
        print(f'Пользователь {user} подключился к БД')
        condition.notify()
        print(f'Пользователь {user} отключается от БД')


async def main() -> None:
    users = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eva', 'Frank', 'George', 'Helen', 'Ivan', 'Julia']
    condition = asyncio.Condition()
    await asyncio.gather(*[asyncio.create_task(connect_to_db(user, condition)) for user in users])

asyncio.run(main())
