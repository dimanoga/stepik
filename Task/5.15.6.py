"""
Задание: Написать асинхронный код, который будет модерировать список сообщений. Каждое сообщение представляет
собой словарь с двумя полями: message_id и message.
Ваша задача - проверить каждое сообщение на наличие запрещенных слов, не учитывая регистр букв,
используйте метод lower().
"""
import asyncio

banned_words = ['ошибка', 'баг', 'отладка', 'память', 'процессор', 'компиляция', 'алгоритм', 'функция', 'база данных',
                'интерфейс']
message = [

    {
        "message_id": 45677,
        "message": " Я думаю, мы должны рассмотреть новый алгоритм для этого задания."
    }
]


async def check_message(message: dict[int, str]):
    for message_word in message.get("message").lower().split():
        if message_word.strip('.,') in banned_words:
            task = asyncio.current_task()
            task.cancel()
            print(f'В сообщении {message.get("message_id")} стоп-слово: task.done(): {task.done()}')
            await asyncio.sleep(0)

    print(f'{message.get("message_id")}: {message.get("message")}')


async def main():
    for msg in message:
        try:
            task = asyncio.create_task(check_message(msg))
            await asyncio.sleep(0)
            await task
        except asyncio.CancelledError:
            pass


asyncio.run(main())
