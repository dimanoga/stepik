import asyncio

players = {
    'DragonSlayer': 0.2,
    'ShadowHunter': 0.6,
    'MagicWizard': 0.8,
    'ElfArcher': 2.0,
    'DarkMage': 1.4,
    'SteelWarrior': 1.6,
    'ThunderBolt': 3.0}


async def enter_dungeon(player, wait_time, barrier):
    await asyncio.sleep(wait_time)
    print(f'{player} готов войти в подземелье')
    try:
        await asyncio.wait_for(barrier.wait(), timeout=5)
        print(f'{player} вошел в подземелье')
    except (asyncio.TimeoutError, asyncio.BrokenBarrierError):
        print(f"{player} не смог попасть в подземелье. Группа не собрана")


async def main():
    barrier = asyncio.Barrier(5)
    await asyncio.gather(*[enter_dungeon(player, players[player], barrier) for player in players])

asyncio.run(main())
