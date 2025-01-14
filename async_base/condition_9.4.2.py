import asyncio

wood_resources_dict = {
    'Деревянный меч': 6,
    'Деревянный щит': 12,
    'Деревянный стул': 24,
}
storage = 0

condition = asyncio.Condition()


async def gather_wood():
    # Код по добыче 2 единиц древесины в секунду
    global storage

    while True:
        # Добыча древесины
        await asyncio.sleep(1)  # Добыча происходит каждую секунду
        storage += 2
        print(f"Добыто 2 ед. дерева. На складе {storage} ед.")

        # Уведомление мастерской о наличии древесины
        async with condition:
            condition.notify_all()


async def craft_item():
    global storage
    for item, required_amount in wood_resources_dict.items():
        while storage < required_amount:
            async with condition:
                await condition.wait()  # Ожидание, пока не накопится достаточно древесины

        # Изготовление предмета
        print(f"Изготовлен {item}.")




async def main():
    # Создаем корутины для добычи и производства
    gather_task = asyncio.create_task(gather_wood())
    craft_task = asyncio.create_task(craft_item())

    # Ждем завершения изготовления предметов
    await craft_task

    # В этом примере можно завершить добычу, если не планируется дальнейшее использование
    gather_task.cancel()

asyncio.run(main())
