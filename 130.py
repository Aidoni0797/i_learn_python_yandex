friends =  {
    'Серёга': 'Оренбург',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

# Здесь ваш код
dict_values = friends.values()

sdict_values = set(dict_values)

for sdict_value in sdict_values:
    print(sdict_value)