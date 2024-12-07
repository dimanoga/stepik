import asyncio
import contextvars

# Контекстная переменная для хранения текущего языка
current_language = contextvars.ContextVar('current_language')


def set_language(language_code):
    current_language.set(language_code)


async def get_greeting():
    greetings = {
        'en': "Hello!",
        'ru': "Привет!",
        'es': "Hola!"
    }
    return greetings[current_language.get()]


async def get_error_message():
    error_messages = {
        'en': "An error occurred.",
        'ru': "Произошла ошибка.",
        'es': "Ocurrió un error."
    }
    return error_messages[current_language.get()]


async def test_user_actions(language_code):
    set_language(language_code)
    print(await get_greeting())
    print(await get_error_message())


async def main():
    await asyncio.gather(*[test_user_actions(language) for language in ('en', 'ru', 'es')])


asyncio.run(main())
