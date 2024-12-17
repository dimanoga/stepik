"""
В текущем примере есть "парсер" для поиска ссылок на zip-файлы. Вам нужно обрабатывать результаты задач,
только если ссылки найдены. То есть в данном случае колбэк должен назначаться только для задач,
 в которых были обнаружены нужные ссылки.
"""
import asyncio
import random

random.seed(5)


def on_data_parsed(task):
    result = task.result()
    print(f"Найдено {len(result)} файлов для скачивания: {result}")


async def parse_data(url):
    await asyncio.sleep(1)
    if random.choice([True, False]):
        file_urls = [f"{url}/example_file.zip"]
    else:
        file_urls = []
    if len(file_urls) > 0:
        task = asyncio.current_task()
        task.add_done_callback(on_data_parsed)
    return file_urls


async def main():
    urls = [
        "https://example.com/data1",
        "https://example.com/data2",
        "https://example.com/data3"
    ]
    await asyncio.gather(*[parse_data(url) for url in urls])


asyncio.run(main())
