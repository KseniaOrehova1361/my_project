"""В модуле processing напишите функцию filter_by_state, которая принимает список словарей и опционально
значение для ключа state (по умолчанию 'EXECUTED').
Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
соответствует указанному значению.
Напишите функцию sort_by_date, которая принимает список словарей и необязательный параметр,
задающий порядок сортировки (по умолчанию — убывание). Функция должна возвращать новый список,
отсортированный по дате (date). """

from typing import Any


def filter_by_state(operation_list: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция фильтрует спиок словарей по заданному параметру"""
    # создаем пустой список для отсортировнных данных
    filtred_operation_list = []
    # запускаем цикл по перебору операций
    for operation in operation_list:
        # сравниваем параметр с заданным значением
        if operation["state"] == state:
            # добавляем подходящие операции в отсортированный список
            filtred_operation_list.append(operation)
    return filtred_operation_list


def sort_by_date(operation_list: list[dict[str, Any]], sorter: bool = True) -> list[dict[str, Any]]:
    """Функция сортирует список операций по дате"""
    sorted_operation_list = sorted(operation_list, key=lambda x: x["date"], reverse=sorter)
    return sorted_operation_list


operation_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

if __name__ == "__main__":
    print(filter_by_state(operation_list, state="EXECUTED"))
    print(sort_by_date(operation_list, sorter=True))
