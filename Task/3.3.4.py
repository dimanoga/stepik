"""
Для решения этой задачи вам потребуется усовершенствовать предыдущую задачу, добавив ещё один счётчик,
 и определить свое время задержки для каждого счетчика.

В этой версии добавьте еще один счетчик - "Counter 3". Мы также добавили словарь delays,
который определяет время задержки для каждого счетчика. Таким образом, каждый счетчик "тикает" с разной скоростью.

Словарь max_counts хранит максимальное значение, на которое каждый счетчик должен быть инкрементирован.

# Словарь с максимальными значениями для каждого счётчика

max_counts = {
    "Counter 1": 10,
    "Counter 2": 5,
    "Counter 3": 15
}
Словарь delays, который определяет время задержки для каждого счетчика.


delays = {
    "Counter 1": 1,
    "Counter 2": 2,
    "Counter 3": 0.5
}
"""

import asyncio

max_counts = {
    "Counter 1": 10,
    "Counter 2": 5,
    "Counter 3": 15
}

counters = {
    "Counter 1": 0,
    "Counter 2": 0,
    "Counter 3": 0
}

delays = {
    "Counter 1": 1,
    "Counter 2": 2,
    "Counter 3": 0.5
}


async def counter(name, delay):
    while counters[name] < max_counts[name]:
        counters[name] += 1
        await asyncio.sleep(delay)
        print(f"{name}: {counters[name]}")


async def main():
    tasks = []
    for counter_name, delay in delays.items():
        task = asyncio.create_task(counter(counter_name, delay))
        tasks.append(task)
    await asyncio.gather(*tasks)


asyncio.run(main())
