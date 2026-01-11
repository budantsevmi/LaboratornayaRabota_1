# TODO Напишите функцию find_common_participants
# TODO Провеьте работу функции с разделителем отличным от запятой

def find_common_participants(group1, group2, separator=","):
    list1 = group1.split(separator)
    list2 = group2.split(separator)
    set1 = set(list1)
    set2 = set(list2)
    common = set1.intersection(set2)
    return sorted(list(common))
print("Тест 1 (с разделителем |):")
test1 = find_common_participants(
    "Иванов|Петров|Сидоров",
    "Петров|Сидоров|Смирнов",
    "|"
)
print(f"Результат: {test1}")
print("\nТест 2 (с разделителем , по умолчанию):")
test2 = find_common_participants(
    "Иванов,Петров,Сидоров",
    "Петров,Сидоров,Смирнов"
)
print(f"Результат: {test2}")
print("\nТест 3 (с разделителем ;):")
test3 = find_common_participants(
    "Иванов;Петров;Сидоров",
    "Петров;Сидоров;Смирнов",
    ";"
)
print(f"Результат: {test3}")