import asyncio

reports = [
    {"name": "Алексей Иванов", "report": "Отчет о прибылях и убытках", "load_time": 5},
    {"name": "Мария Петрова", "report": "Прогнозирование движения денежных средств", "load_time": 4},
    {"name": "Иван Смирнов", "report": "Оценка инвестиционных рисков", "load_time": 3},
    {"name": "Елена Кузнецова", "report": "Обзор операционных расходов", "load_time": 2},
    {"name": "Дмитрий Орлов", "report": "Анализ доходности активов", "load_time": 10}
]


async def download_data(report, cancel_):
    try:
        name, report_name, load_time = report.values()
        match name:
            case "Дмитрий Орлов":
                await cancel_(asyncio.current_task())
            case _:
                await asyncio.sleep(load_time)
                print(f"Отчет: {report_name} для пользователя {name} готов")
    except asyncio.CancelledError:
        print(f"Загрузка отчета {report_name} для пользователя {name} остановлена. Введите новые данные")


async def cancel_task(task):
    task.cancel()
    await asyncio.sleep(0)


async def main():
    await asyncio.gather(*[download_data(rprt, cancel_task) for rprt in reports])


asyncio.run(main())
