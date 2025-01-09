import asyncio

counter = 0


async def move_to_a(lock, name: str, robo_id: int):
    global counter
    async with lock:
        print(f'Робот {name}({robo_id}) передвигается к месту A')
        counter += 1
        print(f'Робот {name}({robo_id}) достиг места A. Место A посещено {counter} раз')


async def main():
    robot_names = ['Электра', 'Механикс', 'Оптимус', 'Симулакр', 'Футуриус']
    await asyncio.gather(*[move_to_a(asyncio.Lock(), name, robo_id) for name, robo_id in zip(robot_names, range(5))])

asyncio.run(main())