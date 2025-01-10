import asyncio
import random

error = None
count = 0
sek = 0


async def monitor_rocket_launches(interrupt_flag):
    global count
    global error
    global sek

    try:
        while not interrupt_flag.is_set():
            # Увеличиваем счетчик запусков
            count += 1

            # С вероятностью 25% устанавливаем ошибку
            if random.choices([True, None], weights=[25, 75])[0]:
                error = True

            # Выводим сообщение о запуске
            print(f"Мониторинг ракетных запусков... (Запуск номер {count} прошёл успешно)")

            # Задержка в 1 секунду перед следующим запуском
            await asyncio.sleep(1)
    finally:
        print("Завершение мониторинга ракетных запусков")


async def main():
    global error
    global count
    global sek

    # Создаем флаг прерывания
    interrupt_flag = asyncio.Event()

    # Создаем Task задачу для мониторинга запусков ракет
    task = asyncio.create_task(monitor_rocket_launches(interrupt_flag))

    while True:
        # Ожидаем 5 секунд перед проверкой состояния
        await asyncio.sleep(5)
        sek += 5

        # Проверяем условия выхода из цикла
        if count >= 50:
            break

        if error:
            print(f"Ошибка при запуске произошла на {sek} секунде =(")
            print("Отмена мониторинга ракетных запусков...")
            interrupt_flag.set()  # Устанавливаем флаг прерывания
            break

        print(f"Время ожидания составило {sek} секунд. За это время ошибки не произошло")

    # Ждем завершения задачи мониторинга
    await task


if __name__ == "__main__":
    asyncio.run(main())
