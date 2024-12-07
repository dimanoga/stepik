import asyncio
import contextvars

order_state = contextvars.ContextVar('order_state')


def set_order_state(state):
    order_state.set(state)


async def process_order(order_id):
    for state in ("Принят", "Обрабатывается", "Отправлен"):
        await asyncio.sleep(.1)
        set_order_state(state)
        print(f"Заказ {order_id} сейчас в состоянии: {order_state.get()}")


async def main():
    orders = ["Заказ1", "Заказ123", "Заказ12345"]
    await asyncio.gather(*[process_order(order) for order in orders])


asyncio.run(main())
