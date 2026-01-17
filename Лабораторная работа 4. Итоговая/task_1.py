# TODO решите задачу
import json


def task() -> float:
    # Читаем данные из файла input.json
    with open('input.json', 'r') as file:
        data = json.load(file)

    # Вычисляем сумму произведений score * weight
    total = sum(item["score"] * item["weight"] for item in data)

    # Округляем до 3 знаков после запятой и возвращаем
    return round(total, 3)


print(task())