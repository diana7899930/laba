def utf8_converter(func):              # створюємо декоратор
    def wrapper(*args, **kwargs):      # обгортка приймає всі аргументи

        result_args = []               # список для нових позиційних аргументів

        # обробляємо всі позиційні аргументи
        for item in args:
            if isinstance(item, str):  # якщо аргумент — рядок
                new_text = item.encode("utf-8")  # переводимо в UTF-8
                result_args.append(new_text)     # додаємо новий
            else:
                result_args.append(item)         # якщо не рядок — залишаємо

        result_kwargs = {}            # словник для нових іменованих аргументів

        # обробка всіх ключових аргументів
        for key, value in kwargs.items():
            if isinstance(value, str):           # якщо значення — рядок
                new_text = value.encode("utf-8")
                result_kwargs[key] = new_text
            else:
                result_kwargs[key] = value       # якщо не рядок — без змін

        # викликаємо оригінальну функцію з новими аргументами
        result = func(*result_args, **result_kwargs)

        return result

    return wrapper
