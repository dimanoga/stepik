"""
Вы — талантливый программист, который получил загадочное письмо от анонимного источника. В письме говорится,
что на определённой веб-странице спрятана последовательность чисел, которая должна быть расшифрована и преобразована
 в буквенную последовательность. Эта последовательность является ключом к секретному хранилищу знаний.

Ваша задача — написать асинхронный код для получения кода со страницы и его расшифровки.
 Ваш код должен сделать всего 1 асинхронный запрос на указанный адрес.

В письме Вам представили словарь code_dict, где каждому числу (от 0 до 9) соответствует определенная буква алфавита.
 Например, числу 0 соответствует буква 'F', числу 1 — буква 'B' и так далее. 1234 == BDJE.


"""
import asyncio

import aiohttp
from bs4 import BeautifulSoup

code_dict = {
    0: 'F',
    1: 'B',
    2: 'D',
    3: 'J',
    4: 'E',
    5: 'C',
    6: 'H',
    7: 'G',
    8: 'A',
    9: 'I'
}


async def get_text_from_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as response:
            soup = BeautifulSoup(await response.text(), 'html.parser')
            p_text = soup.find('p').text.strip()
            return p_text


async def main():
    text = await  get_text_from_url(url='https://asyncio.ru/zadachi/1/index.html')
    result_text = ''.join((code_dict.get(int(number)) for number in text))
    print(result_text)
asyncio.run(main())
