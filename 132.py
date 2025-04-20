english = {
    'рука': 'arm',
    'нога': 'leg',
    'хвост': 'tail',
    'питон': 'python',
    'бэкенд-разработчик': 'back-end developer',
    'голова': 'head'
}

# Объявим новый словарь
new_words = {'мозг': 'brain', 'логика': 'logic'}

# Добавим в словарь english элементы словаря new_words
english.update(new_words)

# Посмотрим, что теперь хранится в словаре english
print(english)

# Заодно выясним, что произошло со словарём new_words
print(new_words)