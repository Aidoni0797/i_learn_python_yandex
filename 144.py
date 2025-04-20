favorite_songs = {
    'Серёга': ['Unforgiven', 'Holiday', 'Highway to hell'],
    'Соня': ['Shake it out', 'The Show Must Go On', 'Наше лето'],
    'Дима': ['Владимирский централ', 'Мурка', 'Третье сентября']
}
# Ниже напишите код, который напечатает на экран, сколько у Димы любимых песен

for key, value in favorite_songs.items():
    if key == 'Дима':
        print(len(value))

# Ниже напишите код, который построчно напечатает
# все любимые песни Сони.
for key, value in favorite_songs.items():
    if key == 'Соня':
        for i in range(0, len(value)):
            print(value[i])