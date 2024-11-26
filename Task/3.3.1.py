"""
Создайте три корутины, которые будут выводить следующие сообщения:

Coroutine 1 is done
Coroutine 2 is done
Coroutine 3 is done
Используя библиотеку asyncio, создайте три задачи для ранее созданных корутин.

Запустите все задачи одновременно, используя asyncio.run()

"""
import asyncio


async def my_coroutine(number):
    print(f'Coroutine {number} is done')


async def main():
    tasks = [asyncio.create_task(my_coroutine(i)) for i in range(1, 4)]
    await asyncio.gather(*tasks)


asyncio.run(main())
