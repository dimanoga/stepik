"""import asyncio


@asyncio.coroutine
def send_message(message):
    print(f"Отправка сообщения: {message}")
    yield from asyncio.sleep(1)  # Имитация задержки отправки сообщения
    print(f"Сообщение отправлено: {message}")


@asyncio.coroutine
def receive_message():
    yield from asyncio.sleep(2)  # Имитация задержки получения сообщения
    message = "И тебе привет!"
    print(f"Сообщение получено: {message}")
    return message


@asyncio.coroutine
def main():
    send_task = asyncio.ensure_future(send_message("Привет"))
    receive_task = asyncio.ensure_future(receive_message())
    yield from asyncio.wait([send_task, receive_task])
    event_loop = asyncio.get_event_loop()
    print(f'Цикл событий активен: {event_loop.is_running()}')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
"""
import asyncio


async def send_message(message):
    print(f"Отправка сообщения: {message}")
    await asyncio.sleep(1)  # Имитация задержки отправки сообщения
    print(f"Сообщение отправлено: {message}")


async def receive_message():
    await asyncio.sleep(2)  # Имитация задержки получения сообщения
    message = "И тебе привет!"
    print(f"Сообщение получено: {message}")
    return message


async def main():
    send_task = asyncio.create_task(send_message("Привет"))
    receive_task = asyncio.create_task(receive_message())
    await asyncio.wait([send_task, receive_task])
    event_loop = asyncio.get_running_loop()
    print(f'Цикл событий активен: {event_loop.is_running()}')


asyncio.run(main())
