beaufort = 7
# Если ветер в 7 или 8 баллов, то он называется крепким
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
    print('Сильный ветер')
elif beaufort == 7 or beaufort == 8:
    print('Крепкий ветер')