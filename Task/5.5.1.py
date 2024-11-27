"""
Создайте асинхронную функцию activate_portal(x), где x — время, необходимое для активации портала.
Функция должна печатать сообщение об активации портала и затем "засыпать" на время x, имитируя процесс активации.
После активации функция возвращает x * 2, что представляет собой количество энергии, выделенной при активации.

Создайте асинхронную функцию perform_teleportation(x), где x — время, необходимое для телепортации.
Функция должна печатать сообщение о процессе телепортации и затем "засыпать" на время x, имитируя процесс телепортации.
После завершения телепортации функция возвращает x + 2, что представляет собой количество времени, использованное в процессе телепортации.
"""
import asyncio


async def activate_portal(x: int):
    print(f'Активация портала в процессе, требуется времени: {x} единиц')
    return await asyncio.sleep(x, result=x * 2)


async def perform_teleportation(x: int):
    print(f'Телепортация в процессе, требуется времени: {x} единиц')
    return await asyncio.sleep(x, result=x + 2)


async def portal_operator():
    portal_task = await asyncio.ensure_future(activate_portal(2))

    energy_to_teleport = portal_task if portal_task < 4 else 1

    teleportation_time = await asyncio.create_task(perform_teleportation(4))
    print(f'Результат активации портала: {energy_to_teleport} единиц энергии')
    print(f'Результат телепортации: {teleportation_time} единиц времени')


asyncio.run(portal_operator())
