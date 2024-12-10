"""
Создайте корутину fetch_weather():
Корутина должна ожидать ответ в течение случайного времени от 1 до 5 секунд включительно.
После ожидания корутина должна "получить" данные о температуре: также случайная величина в диапазоне от -10 до +35
градусов включительно.
Генерируйте случайные значения задержки и температуры методом random.randint() и не меняйте значение random.seed().
Корутина должна возвращать результат в формате:
f"Данные о погоде получены из источника {source} для города {city}: {temperature}°C"
В корутине main() запустите задачи для каждого источника данных, указанного в списке sources, для города указанного в
переменной city. Дождитесь получения ответа от первого источника и выведите результат на экран.
Дожидаться результата остальных задач не нужно.
"""
import asyncio
import random

# Не менять!
random.seed(0)


async def fetch_weather(source, city):
    await asyncio.sleep(random.randint(1, 5))
    temperature = random.randint(-10, 35)
    return f"Данные о погоде получены из источника {source} для города {city}: {temperature}°C"


async def main():
    city = "Москва"
    sources = [
        'http://api.weatherapi.com',
        'http://api.openweathermap.org',
        'http://api.weatherstack.com',
        'http://api.weatherbit.io',
        'http://api.meteostat.net',
        'http://api.climacell.co'
    ]
    tasks = [asyncio.create_task(fetch_weather(source, city)) for source in sources]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    for task in done:
        print(task.result())


asyncio.run(main())
