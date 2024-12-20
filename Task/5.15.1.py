"""
Каждый фейерверк должен сгенерировать два сообщения:

Первое сообщение выводится при "запуске" фейерверка. Оно должно содержать информацию о цвете, форме и действии
фейерверка в формате: f"Запущен {color} {shape} салют, в форме {action}!!!", где {color}, {shape} и
{action} - это одно из значений свойств фейерверка.
Второе сообщение выводится по истечении времени полета фейерверка и сообщает о его "завершении".
Оно должно быть в формате: f"Салют {color} {shape} завершил выступление {action}", где {color},
{shape} и {action} также берутся из списка свойств фейерверка.
"""
import asyncio
import itertools
import random

shapes = ["circle", "star", "square", "diamond", "heart"]
colors = ["red", "blue", "green", "yellow", "purple"]
actions = ["change_color", "explode", "disappear"]
combinations = list(itertools.product(shapes, colors, actions))


class Firework:
    def __init__(self, shape, color, action):
        self.shape = shape
        self.color = color
        self.action = action

    def __str__(self):
        return f"Запущен {self.color} {self.shape} салют, в форме {self.action}!!!"

    async def launch(self):
        print(self)
        await asyncio.sleep(random.randint(1, 5))
        print(f"Салют {self.color} {self.shape} завершил выступление {self.action}")


async def main():
    tasks = []
    for shape, color, action in combinations:
        firework = Firework(shape, color, action)
        task = asyncio.create_task(firework.launch())
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
