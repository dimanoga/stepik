# Максимальное время для каста заклинания
import asyncio

max_cast_time = 5  # Секунды
import asyncio

# Словарь заклинаний со временем каста
spells = {
    "Огненный шар": 3,
    "Ледяная стрела": 2,
    "Щит молний": 4,
    "Призыв зверя": 6,
    "Лечебное зелье": 1,
    "Молния": 5,
    "Водяной щит": 5,
    "Каменная кожа": 4,
    "Иллюзия": 3,
    "Телепортация": 7
}

# Ученики мага
students = ["Алара", "Бренн", "Сирил", "Дариа", "Элвин"]

# Максимальное время каста
max_cast_time = 5  # Секунды


async def cast_spell(student, spell, cast_time):
    await asyncio.sleep(cast_time)
    return f"{student} успешно кастует {spell} за {cast_time} сек."


async def cast_all_spells_for_student(student):
    for spell, cast_time in spells.items():
        task = asyncio.create_task(cast_spell(student, spell, cast_time))
        try:
            await asyncio.wait_for(asyncio.shield(task), max_cast_time)
        except asyncio.TimeoutError:
            await task
            print(
                f"Ученик {student} не справился с заклинанием {spell}, и учитель применил щит. "
                f"{student} успешно завершает заклинание с помощью shield.")
        else:
            print(await task)


async def main():
    tasks = [cast_all_spells_for_student(student) for student in students]
    await asyncio.gather(*tasks)


asyncio.run(main())
