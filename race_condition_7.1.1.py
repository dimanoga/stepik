import asyncio

# Библиотечный каталог
library_catalog = {
    "Мастер и Маргарита": 3,
    "Война и мир": 2,
    "Преступление и наказание": 1,
}

# Резервирование книг для пользователей
reservation_tasks = {
    "Алексей": "Мастер и Маргарита",
    "Ирина": "Мастер и Маргарита",
    "Сергей": "Война и мир",
    "Елена": "Преступление и наказание",
    "Анна": "Мастер и Маргарита",
    "Игорь": "Война и мир",
    "Мария": "Преступление и наказание",
}


async def reserve_book(book_name: str):
    if book_name in library_catalog:
        await asyncio.sleep(1)
        library_catalog[book_name] -= 1
        print("Книга успешно зарезервирована.")
    else:
        print("Книга отсутствует. Резервирование отменено.")


async def main():
    await asyncio.gather(*[reserve_book(book_name) for book_name in reservation_tasks.values()])
    print(f"Мастер и Маргарита: {library_catalog['Мастер и Маргарита']}")
    print(f"Война и мир: {library_catalog['Война и мир']}")
    print(f"Преступление и наказание: {library_catalog['Преступление и наказание']}")

asyncio.run(main())
