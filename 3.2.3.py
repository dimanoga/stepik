"""Создайте корутину generate(), которая принимает число в качестве аргумента и выводит сообщение в формате:
"Корутина generate с аргументом {число}"
Создайте корутину main(). Внутри этой корутины:
Сгенерируйте последовательность чисел от 0 до 9 (включительно).
Для каждого сгенерированного числа создайте асинхронную задачу, передав число в корутину generate().
Запустите все созданные задачи.
Используйте функцию asyncio.run(), чтобы запустить корутину main()."""

import asyncio


async def generate(number):
    print(f'Корутина generate с аргументом {number}')
    await asyncio.sleep(2)


async def main():
    tasks = [asyncio.create_task(generate(i)) for i in range(10)]
    await asyncio.gather(*tasks)


asyncio.run(main())
