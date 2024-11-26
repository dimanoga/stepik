"""
Часто возникает необходимость в последовательном выполнении задач, где результат одной операции служит входными данными
для следующей. Реализуйте такой подход с помощью объектов Task и функции create_task().
Создайте и запустите цепочку асинхронных функций, где каждая последующая функция зависит от результата предыдущей.
"""
import asyncio


async def first_function(x):
    print(f"Выполняется первая функция с аргументом {x}")
    await asyncio.sleep(1)
    result = x + 1
    print(f"Первая функция завершилась с результатом {result}")
    return result


async def second_function(x):
    print(f"Выполняется вторая функция с аргументом {x}")
    await asyncio.sleep(1)
    result = x * 2
    print(f"Вторая функция завершилась с результатом {result}")
    return result


async def third_function(x):
    print(f"Выполняется третья функция с аргументом {x}")
    await asyncio.sleep(1)
    result = x + 3
    print(f"Третья функция завершилась с результатом {result}")
    return result


async def fourth_function(x):
    print(f"Выполняется четвертая функция с аргументом {x}")
    await asyncio.sleep(1)
    result = x ** 2
    print(f"Четвертая функция завершилась с результатом {result}")
    return result


async def main():
    print("Начало цепочки асинхронных вызовов")
    task1 = asyncio.create_task(first_function(1))
    task2 = asyncio.create_task(second_function(await task1))
    task3 = asyncio.create_task(third_function(await task2))
    task4 = asyncio.create_task(fourth_function(await task3))
    await task4
    print(f"Конечный результат цепочки вызовов: {task4.result()}")

asyncio.run(main())
