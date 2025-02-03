"""
Описание задачи:

Вам предоставлены лог-файлы переписок, хранящиеся в папке chat_log.rar.
Каждый файл содержит строки в формате: YYYY-MM-DD HH:MM:SS - Имя Фамилия Отчество: Сообщение.
Необходимо обработать каждый файл и подсчитать стоимость каждого сообщения для каждого участника чата.
Стоимость сообщения рассчитывается как количество символов в сообщении, умноженное на 0,03р за символ.
Посчитайте все символы, включая пробелы.
Выполните округление каждой полученной суммы до 2х символов с помощью round(float(v), 2),
например: 373199.39999999997 => 373199.4р.
После обработки всех файлов необходимо сформировать словарь,
где ключом будет полное имя участника чата, а значением - итоговая сумма, которую он должен заплатить.
Словарь должен быть отсортирован по убыванию суммы.
"""
import asyncio
import json

import os
from collections import defaultdict

import aiofiles

semaphore = asyncio.BoundedSemaphore(1000)
dir = 'C:\\Users\\User\\Downloads\\chat_log'


async def calc_message(file_path, output_dict):
    async with semaphore:
        async with aiofiles.open(file_path, 'r', encoding="utf-8") as f:
            for line in await f.readlines():
                name, message = line[22:].strip().split(': ')
                output_dict[name] += len(message)


async def main():
    output_dict = defaultdict(float)
    tasks = []
    for filename in os.listdir(dir):
        tasks.append(calc_message(os.path.join(dir, filename), output_dict))
    await asyncio.gather(*tasks)
    output_dict = {k: f"{round(v * 0.03, 2)}р" for k, v in sorted(output_dict.items(), key=lambda item: item[1], reverse=True)}
    print(json.dumps(output_dict, ensure_ascii=False, indent=4))


asyncio.run(main())
