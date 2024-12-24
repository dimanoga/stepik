import asyncio
import random

ip_dct = {'192.168.0.1': [0, 100], '192.168.0.2': [225, 300], '192.168.2.5': [150, 185]}


async def scan_port(address, port) -> bool | None:
    """
    Асинхронная функция, имитирующая сканирование порта на заданном ip-адресе.
    """
    await asyncio.sleep(1)
    if random.randint(0, 100) == 1:
        # Печать сообщения об обнаружении открытого порта.
        print(f'Port {port} on {address} is open')
        return port
    return None


async def scan_range(address, start_port, end_port):
    """
    Асинхронная функция, проверяющая состояние диапазона портов по указанному адресу.
    """
    # Печать сообщения о начале сканирования диапазона портов для заданного ip-адреса.
    print(f"Scanning ports {start_port}-{end_port} on {address}")

    result = await asyncio.gather(*[scan_port(address, port) for port in range(start_port, end_port + 1)])
    return address, [port for port in result if port is not None]


async def main(dct):
    """
    Основная асинхронная функция, управляющая процессом сканирования портов из переданного в нее словаря.
    """
    result = await asyncio.gather(
        *[scan_range(address, start_port, end_port) for address, (start_port, end_port) in dct.items()])
    for adress, ports in result:
        if ports:
            print(f'Всего найдено открытых портов {len(ports)} {ports} для ip: {adress}')


# Запуск асинхронного приложения с передачей в main() словаря ip_dct
asyncio.run(main(ip_dct))
