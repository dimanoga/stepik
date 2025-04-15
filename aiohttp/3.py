"""
Файл problem_pages.txt содержит список проблемных страниц, каждая из которых указана на новой строке.
 Эти строки представляют собой имена страниц, которые нужно будет использовать для формирования полных URL-адресов.
 Пример содержимого файла:

10275454
1046410
10660263
Для каждого числа из файла problem_pages.txt, необходимо сформировать полный URL-адрес,
 добавив к нему базовый URL и расширение .html.

Если имя страницы в файле — 10275454, то полный URL будет: https://asyncio.ru/zadachi/2/html/10275454.html

Каждая страница содержит тег <p> с id='number', в котором находится число.
Это число нужно извлечь и добавить к общей сумме. Ваша задача — суммировать все числа со всех страниц находящихся в файле.
"""
import asyncio
import aiofiles
import aiohttp
from bs4 import BeautifulSoup

semaphore = asyncio.Semaphore(15)
number = 0


async def get_number_from_url(url, session):
    global number
    async with semaphore:
        async with session.get(url) as response:
            soup = BeautifulSoup(await response.text(), 'html.parser')
            print(soup)
            p_tags = soup.find('p', id='number').text
            number += int(p_tags)


async def get_problem_numbers():
    async with aiofiles.open('problem_pages.txt', mode='r') as f:
        content = await f.read()
    return content.split('\n')


async def main():
    numbers = await get_problem_numbers()
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            *[get_number_from_url(url=f'https://asyncio.ru/zadachi/2/html/{item}.html', session=session) for item in
              numbers])
    print(number)


asyncio.run(main())
