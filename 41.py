bunny_counter = ''  # Создали переменную bunny_counter, её значение - пустая строка.

for i in range(1, 6):
    # На каждой итерации цикла
    # к переменной bunny_counter будет дописываться
    # очередная цифра, запятая и пробел (чтобы числа в строке не слиплись).
    # Получившееся значение будет присвоено той же переменной bunny_counter
    bunny_counter = bunny_counter + str(i) + ', '

print(bunny_counter + 'вышла iDONi программировать!')