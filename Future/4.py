"""
Допишите корутину waiter(future). Она должна ожидать завершения future (await future).
 После этого корутина должна вывести сообщение.
f"future выполнен, результат {future.result()}. Корутина waiter() может продолжить работу"
Допишите корутину setter(future). Она должна спать случайное время в интервале от 1 до 3 секунд.
После этого установите результат для переданного future в значение True (метод set_result())
В корутине main() создайте объект Future и одновременно запустите 2 задачи, одну для корутины waiter(future),
одну для корутины setter(future) и дождитесь их выполнения (используйте asyncio.gather()).


import asyncio
import random

async def waiter(future):
    pass

async def setter(future):
    pass

async def main():
    pass

asyncio.run(main())

"""
import asyncio
import random


async def waiter(future):
    await future
    print(f"future выполнен, результат {future.result()}. Корутина waiter() может продолжить работу")


async def setter(future):
    await asyncio.sleep(random.randint(1, 3))
    future.set_result(True)
    pass


async def main():
    future = asyncio.Future()
    await asyncio.gather(waiter(future), setter(future))


asyncio.run(main())
