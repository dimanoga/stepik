import asyncio

patient_info = [
    {'name': 'Алексей Иванов', 'direction': 'Терапевт', 'procedure': 'Прием для общего осмотра'},
    {'name': 'Мария Петрова', 'direction': 'Хирург', 'procedure': 'Малая операция'},
    {'name': 'Ирина Сидорова', 'direction': 'ЛОР', 'procedure': 'Осмотр уха'},
    {'name': 'Владимир Кузнецов', 'direction': 'Терапевт', 'procedure': 'Консультация'},
    {'name': 'Елена Васильева', 'direction': 'Хирург', 'procedure': 'Хирургическая процедура'},
    {'name': 'Дмитрий Николаев', 'direction': 'ЛОР', 'procedure': 'Промывание носа'},
    {'name': 'Светлана Михайлова', 'direction': 'Терапевт', 'procedure': 'Рутинный осмотр'},
    {'name': 'Никита Алексеев', 'direction': 'Хирург', 'procedure': 'Операция на колене'},
    {'name': 'Ольга Сергеева', 'direction': 'ЛОР', 'procedure': 'Лечение ангины'},
    {'name': 'Анна Жукова', 'direction': 'Терапевт', 'procedure': 'Вакцинация'}
]


async def producer(queues, patient_info):
    for patient in patient_info:
        queue = queues[patient['direction']]
        await queue.put(patient)
        print(f"Регистратор добавил в очередь: {patient['name']},"
              f" направление: {patient['direction']}, процедура: {patient['procedure']}")
        await asyncio.sleep(0)


async def consumer(queue, doctor_type):
    while True:
        patient = await queue.get()
        print(f"{doctor_type} принял пациента: {patient['name']}, процедура: {patient['procedure']}")
        await asyncio.sleep(0.2)
        queue.task_done()

        if queue.empty():
            break


async def main():
    surgeon_queue = asyncio.Queue()
    ent_queue = asyncio.Queue()
    therapist_queue = asyncio.Queue()
    queues = {'ЛОР': ent_queue,
              'Терапевт': therapist_queue,
              'Хирург': surgeon_queue
              }
    await asyncio.gather(*[asyncio.create_task(producer(queues, patient_info)),
                           asyncio.create_task(consumer(surgeon_queue, 'Хирург')),
                           asyncio.create_task(consumer(ent_queue, 'ЛОР')),
                           asyncio.create_task(consumer(therapist_queue, 'Терапевт'))
                           ])


asyncio.run(main())
