beaufort = 19
# Если ветер шесть баллов или больше
if beaufort >= 6:
    print('Будьте осторожны, сильный ветер!')

# Если ветер в четыре балла или менее
if beaufort <= 4:
    print('Лёгкий ветер')

# Если есть хоть какой-то ветер
if beaufort != 0:
    print('Ветрено')