"""
Условия соревнования:
Дистанция забега: 100 метров.
Участники: 20 бегунов с заранее определенной скоростью.
Цель: Симулируйте забег, где каждый бегун стартует одновременно со всеми, а финиширует в зависимости от своей скорости.
Формула расчёта и округления значения результата до 2-х символов после запятой: round(distance / speed, 2).
Ограничение по времени: Зачетное время на преодоление дистанции бегунами не должно превысить 10 секунд.
Ваша задача - отследить, кто из участников укладывается в это время. Бегуны, не успевшие завершить забег
в течение 10 секунд, в итоговый вывод включаться не должны.
Задача:
Создайте 20 асинхронных задач, по одной для каждого бегуна, где каждая задача будет симулировать время, необходимое
бегуну для завершения забега. Используйте функцию asyncio.create_task() для инициализации каждой задачи,
asyncio.wait_for() для установки максимального времени выполнения всех задач и asyncio.gather()
для одновременного старта бегунов.
"""
import asyncio

runners = {
    "Молния Марк": 12.8,
    "Ветренный Виктор": 13.5,
    "Скоростной Степан": 11.1,
    "Быстрая Белла": 10.8,
    "Легкая Лиза": 11.3,
    "Ракетный Роман": 9.8,
    "Турбо Таня": 13.7,
    "Живчик Женя": 12.5,
    "Вихревой Валерий": 14.5,
    "Газель Галина": 13.4,
    "Непобедимый Никита": 11.7,
    "Прыгун Павел": 10.9,
    "Зефирный Захар": 11.2,
    "Метеор Марина": 9.3,
    "Экспресс Елена": 9.1,
    "Флеш Филипп": 10.2,
    "Аэродинамичная Алина": 8.6,
    "Бриз Борис": 9.4,
    "Ветерок Василий": 13.1,
    "Стрела Станислав": 12.9
}


async def run_lap(name, speed):
    time_needed = round(100 / speed, 2)
    await asyncio.sleep(time_needed)
    print(f"{name} завершил круг за {time_needed} секунд")


async def main(max_time=10):  # Максимальное время для завершения круга 10 сек
    tasks = [asyncio.create_task(run_lap(name, speed)) for name, speed in runners.items()]
    try:
        await asyncio.wait_for(asyncio.gather(*tasks), max_time)
    except asyncio.TimeoutError:
        print("Круг превысил дистанцию")



asyncio.run(main())
