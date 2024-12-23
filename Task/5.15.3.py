import asyncio


# Объявите функцию publish_post: принимает на вход текст поста и имитирует публикацию нового поста на блоге Васи
async def publish_post(text):
    await asyncio.sleep(1)
    output = f"Пост опубликован: {text}"
    print(output)
    return output


# Объявите функцию notify_subscribers: принимает на вход список подписчиков и имитирует отправку уведомления каждому подписчику
async def notify_subscribers(subscribers):
    for subscriber in subscribers:
        await asyncio.sleep(1)
        print(f"Уведомление отправлено {subscriber}")


async def main():
    post_text = "Hello world!"
    subscribers = ["Alice", "Bob", "Charlie", "Dave", "Emma", "Frank", "Grace", "Henry", "Isabella", "Jack"]
    await asyncio.create_task(publish_post(post_text))
    await asyncio.create_task(notify_subscribers(subscribers))
# запускаем асинхронную функцию main()

asyncio.run(main())