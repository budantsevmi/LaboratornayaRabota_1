# TODO импортировать необходимые молули
      # TODO считать содержимое csv файла
      # TODO Сериализовать в файл с отступами равными 4

import csv
import json
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
def task() -> None:
    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, 'r') as csv_file:
        # Просто читаем как есть, без преобразования типов
        reader = csv.DictReader(csv_file)
        data = [dict(row) for row in reader]
    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w') as json_file:
        json.dump(data, json_file, indent=4)
if __name__ == '__main__':
    task()
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")