# config.py
import os
from dotenv import load_dotenv

# Завантажуємо змінні з файлу .env у пам'ять
load_dotenv()

# Отримуємо значення токена
TOKEN = os.getenv("BOT_TOKEN")

# Перевірка (щоб ти відразу бачив помилку, якщо забув створити .env)
if not TOKEN:
    raise ValueError("Помилка: Токен не знайдено! Перевір файл .env")