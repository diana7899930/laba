# main.py
from loader import bot
import handlers.user_handlers  # Імпортуємо хендлери, щоб вони зареєструвалися

if __name__ == '__main__':
    print("Бот запущено modular mode...")
    bot.infinity_polling()