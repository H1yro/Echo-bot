import config
import telebot
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

bot = telebot.TeleBot(config.Test_Python_Question)

telebot.logger.setLevel(logging.INFO)

@bot.message_handler(commands=['start'])
def send_welcome(message):

    logger.info(f"\n--- Новое сообщение ---")
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name if message.from_user.last_name else ''
    username = message.from_user.username if message.from_user.username else 'N/A'
    logger.info(f"Отправитель: {first_name} {last_name} (@{username}) [ID: {user_id}]")
    logger.info(f"Тип сообщения: {message.content_type}")

    bot.reply_to(message, "Привает! Я бот-помощник. Отправь мне фото, видео, аудио ,стикер или текст, и я отвечу тебе тем же!")
    logger.info(f"Ответ пользователю {user_id} отправлен.")

@bot.message_handler(commands=['help'])
def send_help(message):
    logger.info(f"\n--- Новое сообщение ---")
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name if message.from_user.last_name else ''
    username = message.from_user.username if message.from_user.username else 'N/A'
    logger.info(f"Отправитель: {first_name} {last_name} (@{username}) [ID: {user_id}]")
    logger.info(f"Тип сообщения: {message.content_type}")

    help_text = """
Я могу обрабатывать следующие типы сообщений:
- **Фотографии:** Отправь мне фото, и я отправлю его тебе обратно.
- **Видео:** Отправь мне видео, и я отправлю его тебе обратно.
- **Стикеры:** Отправь мне стикер, и я отправлю его тебе обратно.
- **Аудио:** Отправь мне аудио, и я отправлю его тебе обратно.
- **Текст:** Отправь мне текст, и я отвечу тебе тем же.
"""
    bot.send_message(message.chat.id, help_text, parse_mode="Markdown")
    logger.info(f"Ответ пользователю {user_id} отправлен.")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    try:
        logger.info(f"\n--- Новое сообщение ---")
        user_id = message.from_user.id
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name if message.from_user.last_name else ''
        username = message.from_user.username if message.from_user.username else 'N/A'
        logger.info(f"Отправитель: {first_name} {last_name} (@{username}) [ID: {user_id}]")
        logger.info(f"Тип сообщения: {message.content_type}")

        photo_list = message.photo
        if photo_list:
            file_id = photo_list[-1].file_id
            bot.send_photo(message.chat.id, file_id, caption="Вот твое фото!")
            logger.info(f"Фото (File ID: {file_id}) отправлено обратно пользователю {user_id}.")
        else:
            bot.send_message(message.chat.id, "Не удалось получить фотографию.")
            logger.warning(f"Не удалось получить file_id для фотографии от пользователя {user_id}.")
    except Exception as e:
        logger.error(f"Ошибка при обработке фото от {user_id}: {e}")
        bot.send_message(message.chat.id, "Произошла ошибка при обработке фото.")

@bot.message_handler(content_types=['video'])
def handle_video(message):
    try:
        logger.info(f"\n--- Новое сообщение ---")
        # logger.info(f"Полный объект сообщения: {message}")
        user_id = message.from_user.id
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name if message.from_user.last_name else ''
        username = message.from_user.username if message.from_user.username else 'N/A'
        logger.info(f"Отправитель: {first_name} {last_name} (@{username}) [ID: {user_id}]")
        logger.info(f"Тип сообщения: {message.content_type}")

        file_id = message.video.file_id
        bot.send_video(message.chat.id, file_id, caption="Вот твое видео!")
        logger.info(f"Видео (File ID: {file_id}) отправлено обратно пользователю {user_id}.")
    except Exception as e:
        logger.error(f"Ошибка при обработке видео от {user_id}: {e}")
        bot.send_message(message.chat.id, "Произошла ошибка при обработке видео.")

@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    try:
        logger.info(f"\n--- Новое сообщение ---")

        user_id = message.from_user.id
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name if message.from_user.last_name else ''
        username = message.from_user.username if message.from_user.username else 'N/A'
        logger.info(f"Отправитель: {first_name} {last_name} (@{username}) [ID: {user_id}]")
        logger.info(f"Тип сообщения: {message.content_type}")

        file_id = message.sticker.file_id
        bot.send_sticker(message.chat.id, file_id)
        logger.info(f"Стикер (File ID: {file_id}) отправлен обратно пользователю {user_id}.")
    except Exception as e:
        logger.error(f"Ошибка при обработке стикера от {user_id}: {e}")
        bot.send_message(message.chat.id, "Произошла ошибка при обработке стикера.")

@bot.message_handler(content_types=['audio'])
def handle_audio(message):
    try:
        logger.info(f"\n--- Новое сообщение ---")

        user_id = message.from_user.id
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name if message.from_user.last_name else ''
        username = message.from_user.username if message.from_user.username else 'N/A'
        logger.info(f"Отправитель: {first_name} {last_name} (@{username}) [ID: {user_id}]")
        logger.info(f"Тип сообщения: {message.content_type}")

        file_id = message.audio.file_id
        bot.send_audio(message.chat.id, file_id)
        logger.info(f"Аудио (File ID: {file_id}) отправлен обратно пользователю {user_id}.")
    except Exception as e:
        logger.error(f"Ошибка при обработке аудио от {user_id}: {e}")
        bot.send_message(message.chat.id, "Произошла ошибка при обработке аудио.")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    try:
        logger.info(f"\n--- Новое сообщение ---")
        user_id = message.from_user.id
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name if message.from_user.last_name else ''
        username = message.from_user.username if message.from_user.username else 'N/A'
        logger.info(f"Отправитель: {first_name} {last_name} (@{username}) [ID: {user_id}]")
        logger.info(f"Тип сообщения: {message.content_type}")
        logger.info(f"Текст сообщения: '{message.text}'")

        bot.reply_to(message, f"Ты написал: {message.text}")
        logger.info(f"Ответ пользователю {user_id} отправлен.")
    except Exception as e:
        logger.error(f"Ошибка при обработке текста от {user_id}: {e}")
        bot.send_message(message.chat.id, "Произошла ошибка при обработке текста.")

@bot.message_handler(func=lambda message: True)
def handle_other(message):
    logger.info(f"\n--- Новое сообщение ---")

    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name if message.from_user.last_name else ''
    username = message.from_user.username if message.from_user.username else 'N/A'
    logger.info(f"Отправитель: {first_name} {last_name} (@{username}) [ID: {user_id}]")
    logger.info(f"Тип сообщения: {message.content_type}")

    logger.warning(f"Получено сообщение неизвестного типа от {user_id}. Тип: {message.content_type}")
    bot.send_message(message.chat.id, "Я не знаю, как обрабатывать этот тип сообщения.")

if __name__ == '__main__':
    logger.info("Бот запускается...")
    bot.polling(none_stop=True, interval=0)
    logger.info("Бот остановлен.")
