import asyncio
import csv
import json

import aiofiles
from aiocsv import AsyncDictReader


class CustomDialect(csv.Dialect):
    delimiter = ';'  # Определяет символ-разделитель столбцов в csv файле как ";"
    quotechar = '"'  # Определяет символ кавычек, используемый для обрамления полей в csv файле, как двойные кавычки ("")
    doublequote = True  # Если этот параметр True, две кавычки внутри поля трактуются как одна кавычка
    skipinitialspace = True  # Если параметр True, пробелы в начале каждого поля игнорируются
    lineterminator = '\n'  # Определяет символ окончания строки в csv файле как "\n"
    quoting = csv.QUOTE_MINIMAL  # Указывает, что кавычки должны окружать только те поля, которые содержат специальные символы (например, разделитель, кавычки или любой из символов новой строки)


csv.register_dialect('customDialect',
                     CustomDialect)  # Регистрирует диалект с именем 'customDialect' для последующего использования в csv.reader или csv.writer

result = []


async def read_csv():
    async with aiofiles.open('', 'r', encoding='utf-8-sig') as f:
        async for row in AsyncDictReader(f, fieldnames=['Идентификатор объекта',
                                                        'Адрес недвижимости',
                                                        'Тип недвижимости',
                                                        'Площадь объекта',
                                                        'Цена',
                                                        'Количество комнат',
                                                        'Состояние объекта',
                                                        'Контактные данные собственника',
                                                        'Статус объекта',
                                                        'Дата добавления информации'
                                                        ],
                                         dialect='customDialect'):
            if row['Идентификатор объекта'] == 'Идентификатор объекта':
                continue
            result.append(row)
    async with aiofiles.open("capitals.json", "w", encoding='utf-8') as my_file:
        await my_file.write(json.dumps(result, indent=4, separators=(',', ':'), ensure_ascii=False))


async def main():
    await read_csv()


asyncio.run(main())
