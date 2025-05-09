import asyncio

tasks_dependencies = {
    "Подготовка_окружения": {
        "этапы": [
            {"название": "Настройка виртуального окружения", "время": 1},
            {"название": "Установка базовых зависимостей", "время": 2},
            {"название": "Настройка системы контроля версий", "время": 3},
            {"название": "Проверка сетевых настроек", "время": 4},
            {"название": "Клонирование основной ветки", "время": 4},
            {"название": "Проверка последних изменений", "время": 6},
            {"название": "Проверка локальных зависимостей", "время": 8}
        ]
    },
    "Проверка_зависимостей": {
        "этапы": [
            {"название": "Обновление устаревших зависимостей", "время": 1},
            {"название": "Установка новых зависимостей", "время": 3},
            {"название": "Предварительная очистка", "время": 6},
            {"название": "Компиляция исходного кода ядра", "время": 4},
            {"название": "Логирование результатов компиляции", "время": 7}
        ]
    },
    "Компиляция_модулей": {
        "этапы": [
            {"название": "Компиляция модуля A", "время": 3},
            {"название": "Компиляция модуля B", "время": 4},
            {"название": "Тестирование модулей на совместимость", "время": 1},
            {"название": "Инициализация тестового окружения", "время": 3},
            {"название": "Тестирование модуля A", "время": 1}
        ]
    },
    "Сборка_БД": {
        "этапы": [
            {"название": "Создание структуры БД", "время": 2},
            {"название": "Наполнение начальными данными", "время": 6},
            {"название": "Импорт данных пользователей", "время": 2},
            {"название": "Импорт транзакционных данных", "время": 1},
            {"название": "Подготовка пакетов для релиза", "время": 4}
        ]
    },
    "Развертывание_релиза": {
        "этапы": [
            {"название": "Создание инструкций для установки", "время": 7},
            {"название": "Финальное тестирование релиза", "время": 1},
            {"название": "Развертывание сборки", "время": 4},
            {"название": "Проверка работоспособности сервисов", "время": 6},
            {"название": "Подготовка релизных заметок", "время": 6},
            {"название": "Финализация документации", "время": 4},
            {"название": "Размещение релиза на сервере обновлений", "время": 1},
            {"название": "Подготовка мероприятия", "время": 3},
            {"название": "Объявление об успешном релизе", "время": 4}
        ]
    }
}


async def execute_subtask(task_name, duration):
    fail = ''
    try:
        await asyncio.sleep(duration)
    except asyncio.CancelledError:
        fail = 'не '
    print(f'Подзадача: {task_name} {fail}успела выполниться в срок, за {duration} сек.')


async def execute_task(task_name, subtasks: list[dict[str, int]]):
    tasks = [asyncio.create_task(execute_subtask(*subtask.values())) for subtask in subtasks]

    try:
        await asyncio.wait_for(asyncio.gather(*tasks), timeout=5)
        print(f'Задача: {task_name} = все подзадачи выполнены')
    except asyncio.TimeoutError:
        print(f'Задача: {task_name} не выполнилась в срок, '
              f'т.к. одна или несколько подзадач заняли слишком много времени.')


async def main():
    await asyncio.gather(
        *[execute_task(task_name, subtasks.get('этапы')) for task_name, subtasks in tasks_dependencies.items()]
    )


asyncio.run(main())
