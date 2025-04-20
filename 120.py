def get_together_games(games_1, games_2):
    game_1 = set(games_1)
    game_2 = set(games_2)
    game_3  = game_1.intersection(game_2)
    # Напишите здесь код функции для поиска пересечений
    return game_3

anfisa_games = [
    'Online-chess',
    'Города',
    'DOOM',
    'Крестики-нолики'
]
alisa_games = [
    'DOOM',
    'Online-chess',
    'Города',
    'GTA',
    'World of tanks'
]
# Вызовите функцию со списками игр в качестве параметров
together_games = get_together_games(anfisa_games, alisa_games)
# Напечатайте итоговый перечень игр в цикле
for together_game in together_games:
    print(f"👾 {together_game}")

# iDONi система приняла но не компилируется в компе интересно как он прочитал этот эмоджи