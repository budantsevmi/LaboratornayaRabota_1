list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# Определяем общее количество игроков в списке
total_players = len(list_players)


# Находим индекс середины списка
middle_index = total_players // 2

# Разделяем игроков на две команды с использованием слайсинга
first_team = list_players[:middle_index]  # первая половина
second_team = list_players[middle_index:]  # вторая половина

print( first_team )
print( second_team )