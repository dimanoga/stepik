import asyncio


async def move_sensor(event, sensor_number, sensor_ip):
    print(f'Датчик {sensor_number} IP-адрес {sensor_ip} настроен и ожидает срабатывания')
    await event.wait()
    print(f'Датчик {sensor_number} IP-адрес {sensor_ip} активирован, "Wee-wee-wee-wee"')


async def send_event(event):
    await asyncio.sleep(5)
    print('Датчики зафиксировали движение')
    event.set()


async def main():
    event = asyncio.Event()
    ip = ["192.168.0.3", "192.168.0.1", "192.168.0.2", "192.168.0.4", "192.168.0.5"]
    asyncio.create_task(send_event(event))
    await asyncio.gather(*[move_sensor(event, number, ip) for number, ip in enumerate(ip)])


asyncio.run(main())
