# handlers/user_handlers.py
from telebot import types
from loader import bot
from services.calculator import generate_result_text


# --- Обробка команди /start ---
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("💘 Перевірити сумісність")
    markup.add(btn)

    bot.send_message(
        message.chat.id,
        f"Привіт, {message.from_user.first_name}! 👋\n"
        "Я розділив код на модулі!\n"
        "Введи команду: `/love Ім'я1 Ім'я2` або натисни кнопку.",
        reply_markup=markup
    )


# --- Обробка команди /love ---
@bot.message_handler(commands=['love'])
def check_compatibility_command(message):
    try:
        args = message.text.split()[1:]
        if len(args) < 2:
            bot.reply_to(message, "Вкажи два імені.\nПриклад: `/love Ромео Джульєтта`")
            return

        result = generate_result_text(args[0], args[1])
        bot.send_message(message.chat.id, result, parse_mode='Markdown')

    except Exception:
        bot.reply_to(message, "Помилка! Спробуй ще раз.")


# --- Обробка натискання кнопки та тексту ---
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "💘 Перевірити сумісність":
        msg = bot.send_message(message.chat.id, "Введи імена (напр: Катя Ваня):")
        bot.register_next_step_handler(msg, process_names_step)
    else:
        # Перевірка, чи ввів користувач просто два імені
        words = message.text.split()
        if len(words) == 2:
            result = generate_result_text(words[0], words[1])
            bot.send_message(message.chat.id, result, parse_mode='Markdown')


def process_names_step(message):
    names = message.text.split()
    if len(names) >= 2:
        result = generate_result_text(names[0], names[1])
        bot.send_message(message.chat.id, result, parse_mode='Markdown')
    else:
        bot.send_message(message.chat.id, "Потрібно два імені!")