"""
Ваша задача: распутать цепочку корутин. Для этого:

Проанализируйте код ниже и определите корутину, которая является точкой входа в программу
Передайте эту корутину в метод asyncio.run()

Sample Output:

Вызываю корутину 3
Вызываю корутину 2
Вызываю корутину 4
Вызываю корутину 1
Вызываю корутину 0

###################################################
import asyncio


async def coro_1():
    print("Вызываю корутину 0")


async def coro_5():
    print("Вызываю корутину 3")
    await coro_3()


async def coro_3():
    print("Вызываю корутину 2")
    await coro_2()


async def coro_4():
    print("Вызываю корутину 1")
    await coro_1()


async def coro_2():
    print("Вызываю корутину 4")
    await coro_4()


asyncio.run()
"""
import asyncio


async def coro_1():
    print("Вызываю корутину 0")


async def coro_5():
    print("Вызываю корутину 3")
    await coro_3()


async def coro_3():
    print("Вызываю корутину 2")
    await coro_2()


async def coro_4():
    print("Вызываю корутину 1")
    await coro_1()


async def coro_2():
    print("Вызываю корутину 4")
    await coro_4()


async def main():
    await coro_5()


asyncio.run(main())
