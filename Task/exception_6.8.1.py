import asyncio

files = ['image.png', 'file.csv', 'file1.txt', 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt', 'file6.txt',
         'file7.txt', 'file8.txt', 'file9.txt', 'file10.txt', 'file11.txt', 'file12.txt', 'file13.txt', 'file14.txt',
         'file15.txt', 'file16.txt', 'file17.txt', 'file18.txt', 'file19.txt', 'file20.txt', 'file21.txt', 'file22.txt',
         'file23.txt', 'file24.txt', 'file25.txt', 'file26.txt', 'file27.txt', 'file28.txt', 'file29.txt', 'file30.txt',
         'file31.txt', 'file32.txt', 'file33.txt', 'file34.txt', 'file35.txt', 'file36.txt', 'file37.txt', 'file38.txt',
         'file39.txt', 'file40.txt', 'file41.txt', 'file42.txt', 'file43.txt', 'file44.txt', 'file45.txt', 'file46.txt',
         'file47.txt', 'file48.txt', 'file49.txt', 'file50.txt', 'file51.txt', 'file52.txt', 'file53.txt', 'file54.txt',
         'file55.txt', 'file56.txt', 'file57.txt', 'file58.txt', 'file59.txt', 'file60.txt', 'file61.txt', 'file62.txt',
         'file63.txt', 'file64.txt', 'file65.txt', 'file66.txt', 'file67.txt', 'file68.txt', 'file69.txt', 'file70.txt',
         'file71.txt', 'file72.txt', 'file73.txt', 'file74.txt', 'file75.txt', 'file76.txt', 'file77.txt', 'file78.txt',
         'file79.txt', 'file80.txt', 'file81.txt', 'file82.txt', 'file83.txt', 'file84.txt', 'file85.txt', 'file86.txt',
         'file87.txt', 'file88.txt', 'file89.txt', 'file90.txt', 'file91.txt', 'file92.txt', 'file93.txt', 'file94.txt',
         'file95.txt', 'file96.txt', 'file97.txt', 'file98.txt', 'file99.txt']

missed_files = ['file4.txt', 'file6.txt', 'file8.txt', 'file12.txt', 'file18.txt', 'file24.txt', 'file29.txt',
                'file38.txt', 'file40.txt', 'file41.txt', 'file58.txt', 'file79.txt']


# Не менять функцию
async def download_file(file_name):
    await asyncio.sleep(1)
    if file_name in missed_files:
        raise FileNotFoundError(f'Файл {file_name} не найден')
    else:
        await asyncio.sleep(1)
        return f'Файл {file_name} успешно скачан'


# Ваш код пишите тут:
async def main():
    tasks = [asyncio.create_task(download_file(file_name)) for file_name in files]

    await asyncio.gather(*tasks, return_exceptions=True)

    for task in tasks:
        if task.exception():
            print(task.exception())


asyncio.run(main())
