import asyncio


async def activate_portal(x: int):
    print(f'Активация портала в процессе, требуется времени: {x} единиц')
    return await asyncio.sleep(x, result=f'Результат активации портала: {x * 2} единиц энергии')


async def perform_teleportation(x: int):
    print(f'Телепортация в процессе, требуется времени: {x} единиц')
    return await asyncio.sleep(x, result=f'Результат телепортации: {x + 2} единиц времени')


async def recharge_portal(x: int):
    print(f'Подзарядка портала, требуется времени: {x} единиц')
    return await asyncio.sleep(x, result=f'Результат подзарядки портала: {x * 3} единиц энергии')


async def check_portal_stability(x: int):
    print(f'Проверка стабильности портала, требуется времени: {x} единиц')
    return await asyncio.sleep(x, result=f'Результат проверки стабильности {x + 4} единиц времени')


async def restore_portal(x: int):
    print(f'Восстановление портала, требуется времени: {x} единиц')
    return await asyncio.sleep(x, result=f'Результат восстановления портала: {x * 5} единиц энергии')


async def close_portal(x: int):
    print(f'Закрытие портала, требуется времени: {x} единиц')
    return await asyncio.sleep(x, result=f'Результат закрытия портала: {x - 1} единиц времени')


async def portal_operator():
    activate_portal_task = asyncio.ensure_future(activate_portal(2))
    perform_teleportation_task = asyncio.ensure_future(perform_teleportation(3))
    recharge_portal_task = asyncio.ensure_future(recharge_portal(4))
    check_portal_stability_task = asyncio.ensure_future(check_portal_stability(5))
    restore_portal_task = asyncio.ensure_future(restore_portal(6))
    close_portal_task = asyncio.ensure_future(close_portal(7))
    result = await asyncio.gather(activate_portal_task,
                                  perform_teleportation_task,
                                  recharge_portal_task,
                                  check_portal_stability_task,
                                  restore_portal_task,
                                  close_portal_task)

    print(f"Результат активации портала: {result[0]} единиц энергии\n"
          f"Результат телепортации: {result[1]} единиц времени\n"
          f"Результат подзарядки портала: {result[2]} единиц энергии\n"
          f"Результат проверки стабильности: {result[3]} единиц времени\n"
          f"Результат восстановления портала: {result[4]} единиц энергии\n"
          f"Результат закрытия портала: {result[5]} единиц времени")


asyncio.run(portal_operator())
