import json


def get_writers_list(filename):
    """
    Получаем из json файла данные в виде списка словарей
    """
    with open(filename, encoding='utf-8') as file:
       writers_data = json.load(file)
    return writers_data




