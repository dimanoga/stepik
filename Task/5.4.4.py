"""
Цель данной задачи - научиться создавать и управлять задачами на основе их имен.


Вам предоставлен список из 10 статусов, который включает в себя состояния от "Отлично" до "Катастрофически".
Этот список будет использоваться для имитации проверки состояния каждого компонента системы.

    status_list = [
        "Отлично", "Хорошо", "Удовлетворительно", "Средне",
        "Пониженное", "Ниже среднего", "Плохо", "Очень плохо",
        "Критично", "Катастрофически"
    ]

Напишите три корутины (monitor_cpu(), monitor_memory(), monitor_disk_space()), каждая из которых отвечает за
мониторинг определенного компонента системы. Каждая корутина должна проходить через список статусов,
имитируя процесс проверки состояния компонента.

При создании асинхронных задач с помощью asyncio.create_task() укажите уникальное имя для каждой задачи
с помощью аргумента name.

asyncio.create_task(..., name="CPU")
Используйте следующие имена задач:

"CPU",
"Память"
"Дисковое пространство"

Внутри каждой корутины используйте asyncio.current_task().get_name() для получения имени текущей задачи.
Это имя затем используется в функции print() для динамического вывода статуса проверки,
делая сообщения более информативными и понятными.

[CPU] Статус проверки: Отлично

print(f"[{task_name}] Статус проверки: {status}")

Если в процессе проверки обнаруживается статус "Катастрофически", корутина должна выводить сообщение о
достижении критического состояния и инициировать "остановку" (имитацию остановки системы).

[CPU] Критическое состояние достигнуто. Инициируется остановка...

print(f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")

В главной корутине main() создайте и запустите все задачи мониторинга конкурентно, используя await asyncio.gather(),
чтобы ожидать их завершения.

"""
import asyncio


async def monitor_cpu(status_list: list[str]):
    task_name = asyncio.current_task().get_name()
    for status in status_list:
        print(f"[{task_name}] Статус проверки: {status}")
        if status == "Катастрофически":
            print(f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")
            break
        await asyncio.sleep(0)


async def monitor_memory(status_list: list[str]):
    task_name = asyncio.current_task().get_name()
    for status in status_list:
        print(f"[{task_name}] Статус проверки: {status}")
        if status == "Катастрофически":
            print(f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")
            break
        await asyncio.sleep(0)


async def monitor_disk_space(status_list: list[str]):
    task_name = asyncio.current_task().get_name()
    for status in status_list:
        print(f"[{task_name}] Статус проверки: {status}")
        if status == "Катастрофически":
            print(f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")
            break
        await asyncio.sleep(0)



async def main():
    status_list = [
        "Отлично", "Хорошо", "Удовлетворительно", "Средне",
        "Пониженное", "Ниже среднего", "Плохо", "Очень плохо",
        "Критично", "Катастрофически"
    ]
    cpu_task = asyncio.create_task(monitor_cpu(status_list), name="CPU")
    memory_task = asyncio.create_task(monitor_memory(status_list), name="Память")
    disk_space_task = asyncio.create_task(monitor_disk_space(status_list), name="Дисковое пространство")
    await asyncio.gather(cpu_task, memory_task, disk_space_task)

asyncio.run(main())
