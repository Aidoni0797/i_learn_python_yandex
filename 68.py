# Код функции say_hello()
def say_hello(current_hour):
    if current_hour <= 5 or current_hour >= 23:
        print('Доброй ночи, iDONi!')
    elif current_hour >= 6 and current_hour <= 11:
        print('Доброе утро, iDONi!')
    elif current_hour >= 12 and current_hour <= 17:
        print('Добрый день, iDONi!')
    elif current_hour >= 18 and current_hour <= 22:
        print('Добрый вечер, iDONi!')

# Дальше код написан без отступов: этот код уже вне функции.

# Несколько раз вызовем функцию say_hello() с разными аргументами:
say_hello(4)  # Вызов функции say_hello() с аргументом 4
say_hello(10)  # Вызов функции с аргументом 10
say_hello(15)  # Ещё один вызов функции
say_hello(20)  # И ещё один вызов