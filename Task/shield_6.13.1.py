# Время доставки до разных городов:
import asyncio

delivery_times = {
    'Москва': 1,
    'Санкт-Петербург': 3,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 4,
    'Челябинск': 6,
    'Омск': 7,
    'Красноярск': 8,
    'Владивосток': 9,
    'Хабаровск': 9
}

# Заказы:
orders = [('Новогодняя кружка', 'Москва', 'нет'), ('Шоколадный набор', 'Красноярск', 'нет'),
          ('Ручка и блокнот', 'Новосибирск', 'важно'), ('Носки с новогодним принтом', 'Владивосток', 'нет'),
          ('Плед', 'Омск', 'нет')]

# Время до нового года:
days_left = 3


# Тут пишите ваш код:
async def deliver(order):
    item, city, _ = order
    await asyncio.sleep(delivery_times[city])
    print(f'Подарок {item} успешно доставлен в г. {city}')


async def main():
    tasks = []
    for order in orders:
        item, city, mark = order
        if mark == 'важно':
            tasks.append(asyncio.shield(deliver(order)))
        else:
            tasks.append(asyncio.create_task(deliver(order)))
    done, pending = await asyncio.wait(tasks, timeout=days_left)
    [future.cancel() for future in pending]
    for task in [task for task in asyncio.all_tasks() if task.get_name() != 'Task-1']:
        if task.get_name() != 'Task-1':
            try:
                await task
            except asyncio.CancelledError:
                pass


asyncio.run(main())
