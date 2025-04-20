favourites_songs_and_ratings = {}

def add_favourite_song(song_name, rank):
    favourites_songs_and_ratings[song_name] = rank

# Словарь пока что пуст:
print('Первый вывод на печать: ', favourites_songs_and_ratings)

add_favourite_song('Гражданская Оборона - Моя оборона', 5)

# А здесь словарь уже обновлен и не пуст:
print('Второй вывод на печать: ', favourites_songs_and_ratings)