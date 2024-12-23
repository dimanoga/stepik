"""
Ваша задача:

Напишите программу для имитации выполнения асинхронных сетевых запросов с помощью asyncio.sleep().
Программа должна просканировать все порты на указанном маршрутизаторе в заданном диапазоне портов.
В качестве имитации вариантов открытого или закрытого порта используйте модуль random который с вероятностью
50% решал бы, закрыт порт или открыт.

IP маршрутизатора: 192.168.0.1
Диапазон для сканирования, порты: 80-85
"""
import random
import asyncio


async def scan_port(address: str, port: int, ) -> int:
    await asyncio.sleep(1)
    if random.randint(0, 1) == 1:
        print(f'Порт {port} на адресе {address} открыт')
        return port


async def scan_range(address, start_port, end_port):
    print(f'Сканирование портов с {start_port} по {end_port} на адресе {address}')
    tasks = []
    for port in range(start_port, end_port + 1):
        task = asyncio.create_task(scan_port(address, port))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    open_ports = [port for port in results if port]
    if open_ports:
        print(f'Открытые порты на адресе {address}: {open_ports}')
    else:
        print(f'Открытых портов на адресе {address} не найдено')


asyncio.run(scan_range('192.168.0.1', 80, 85))
