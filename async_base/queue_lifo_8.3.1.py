import asyncio
from asyncio import LifoQueue


async def autosave(queue):
    time = 0
    while time < 20:
        time += 1
        print(f"Автосохранение игры через {time} часов")
        await queue.put(time)
        await asyncio.sleep(0.1)


async def simulate_gameplay(queue):
    while True:
        autosave = await queue.get()
        if autosave % 5 == 0:
            print(f"Загружена последняя версия игры: Автосохранение {autosave}")
            await asyncio.sleep(0)
        if autosave == 20:
            break


async def main():
    queue = LifoQueue()

    await asyncio.gather(*[asyncio.create_task(simulate_gameplay(queue)),
                           asyncio.create_task(autosave(queue))])
    print('Игра пройдена!')


asyncio.run(main())
