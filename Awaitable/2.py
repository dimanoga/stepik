"""
Данные студентов:
students = {
    "Алекс": {"course": "Асинхронный Python", "steps": 515, "speed": 78},
    "Мария": {"course": "Многопоточный Python", "steps": 431, "speed": 62},
    "Иван": {"course": "WEB Парсинг на Python", "steps": 491, "speed": 57}
}
course — название курса, который проходит студент.
steps — общее количество степов в курсе.
speed — скорость чтения студента в степах в час.
Ваша задача — написать асинхронный код , который позволит всем трем студентам одновременно начать прохождение выбранных
ими курсов и корректно рассчитает время, затраченное каждым из них на обучение. Время прохождения курса должно быть
вычислено по формуле reading_time = steps / speed, где reading_time — время в часах, необходимое для прохождения курса.

"""
import asyncio

students = {
    "Алекс": {"course": "Асинхронный Python", "steps": 515, "speed": 78},
    "Мария": {"course": "Многопоточный Python", "steps": 431, "speed": 62},
    "Иван": {"course": "WEB Парсинг на Python", "steps": 491, "speed": 57}
}


async def study_course(student, course, steps, speed):
    print(f'{student} начал проходить курс {course}.')
    reading_time = round(steps / speed, 2)
    await asyncio.sleep(reading_time)
    print(f'{student} прошел курс {course} за {reading_time} ч.')
    pass


async def main():
    tasks = [study_course(student=student,
                          course=course['course'],
                          steps=course['steps'],
                          speed=course['speed']) for student, course in students.items()]
    await asyncio.gather(*tasks)

    # Ожидание завершения каждой задачи индивидуально


asyncio.run(main())
