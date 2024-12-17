"""
Усовершенствуем предыдущую задачу, добавив в неё условие, которое проверяет, является ли код четным или нечетным
(основываясь на последнем символе в коде), и в зависимости от этого выводит разные сообщения.
Если код содержит чётное число последним символом, то необходимо вывести следующее сообщение, вместо первоначального.

Сообщение: Неверный код, сообщение скрыто
"""
import asyncio

codes = ["56FF4D", "A3D2F7", "B1C94A", "F56A1D", "D4E6F1",
         "A1B2C3", "D4E5F6", "A7B8C9", "D0E1F2", "A3B4C5",
         "D6E7F8", "A9B0C1", "D2E3F4", "A5B6C7", "D8E9F2"]
messages = ["Привет, мир!", "Как дела?", "Что нового?", "Добрый день!", "Пока!",
            "Спокойной ночи!", "Удачного дня!", "Всего хорошего!", "До встречи!", "Счастливого пути!",
            "Успехов в работе!", "Приятного аппетита!", "Хорошего настроения!", "Спасибо за помощь!",
            "Всего наилучшего!"]


def print_code(task) -> None:
    message = task.result()
    code_index = messages.index(message)
    print(f'Код: {codes[code_index]}')


async def print_message(message: str) -> str:
    code = codes[messages.index(message)]
    message_to_print = message

    if code[-1].isdigit():
        if int(code[-1]) % 2 == 0:
            message_to_print = "Неверный код, сообщение скрыто"
    else:
        if int(code[-1], 16) % 2 == 0:
            message_to_print = "Неверный код, сообщение скрыто"
    print(f'Сообщение: {message_to_print}')
    return message


async def main() -> None:
    for message in messages:
        task = asyncio.create_task(print_message(message))
        task.add_done_callback(print_code)
        await task


asyncio.run(main())
