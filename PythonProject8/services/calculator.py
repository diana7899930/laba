# services/calculator.py
import random


def calculate_compatibility() -> int:
    """Генерує випадкове число від 0 до 100"""
    return random.randint(0, 100)


def get_progress_bar(percent: int) -> str:
    """Малює смужку прогресу"""
    length = 10
    filled = int(length * percent // 100)
    return '❤️' * filled + '🤍' * (length - filled)


def get_verdict(percent: int) -> str:
    """Повертає текст залежно від відсотка"""
    if percent <= 20:
        return "😱 Ой лишенько... Краще залишайтеся друзями."
    elif percent <= 40:
        return "🤔 Є сумніви, але спробувати можна."
    elif percent <= 60:
        return "😐 50/50. Як карта ляже."
    elif percent <= 80:
        return "🔥 Дуже гаряче! Чудова пара."
    else:
        return "💍 Це доля! Коли весілля?"


def generate_result_text(name1: str, name2: str) -> str:
    """Збирає повну відповідь"""
    percent = calculate_compatibility()
    bar = get_progress_bar(percent)
    verdict = get_verdict(percent)

    return (
        f"📊 **Результат сумісності:**\n"
        f"👤 {name1} + 👤 {name2}\n\n"
        f"[{bar}] {percent}%\n\n"
        f"{verdict}"
    )