beaufort = 9
# если ветер от 9 до 11 баллов, то это шторм (различной силы)
if beaufort == 0:
    print('Штиль')
elif beaufort == 1:
    print('Тихий ветер')
elif beaufort == 2:
    print('Лёгкий ветер')
elif beaufort == 3:
    print('Слабый ветер')
elif beaufort == 4:
    print('Умеренный ветер')
elif beaufort == 5:
    print('Свежий ветер')
elif beaufort == 6:
    print('Сильный')
elif beaufort == 7 or beaufort == 8:
    print('Крепкий ветер')
elif beaufort >= 9 and beaufort <= 11:
    print('Шторм')
elif beaufort == 12:
    print('Ураган')
else:  # else тоже может быть в конце, после цепочки elif
    print('Неизвестное значение')