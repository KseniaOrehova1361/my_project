"""
Функция filter_by_state:
Тестирование фильтрации списка словарей по заданному статусу
state.
Проверка работы функции при отсутствии словарей с указанным статусом
state в списке.
Параметризация тестов для различных возможных значений статуса state.

Функция sort_by_date:
Тестирование сортировки списка словарей по датам в порядке убывания и возрастания.
Проверка корректности сортировки при одинаковых датах.
Тесты на работу функции с некорректными или нестандартными форматами дат.
"""

import pytest

from src.processing import filter_by_state, sort_by_date

def test_filter_by_state(my_operation_list, filtered_executed):
    assert filter_by_state(my_operation_list) == filtered_executed


def test_filter_by_state_without_state(operation_list_without_executed):
    assert filter_by_state(operation_list_without_executed) == "Операции отсутствуют"


@pytest.mark.parametrize('operation_list, state, expected', [([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                                                               {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                                                               {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                                                               {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}],
                                                              "EXECUTED",
                                                              [{"id": 41428829, "state": "EXECUTED",
                                                                "date": "2019-07-03T18:35:29.512364"},
                                                               {"id": 939719570, "state": "EXECUTED",
                                                                "date": "2018-06-30T02:08:58.425572"}]),
                                                             ([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                                                               {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                                                               {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                                                               {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}],
                                                              "CANCELED",
                                                              [{"id": 594226727, "state": "CANCELED",
                                                                "date": "2018-09-12T21:27:25.241689"},
                                                               {"id": 615064591, "state": "CANCELED",
                                                                "date": "2018-10-14T08:21:33.419441"}])])
def test_filter_by_state_different_state(operation_list, state, expected):
    assert filter_by_state(operation_list, state) == expected


@pytest.mark.parametrize('operation_list, sorter, expected', (([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                                                               {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                                                               {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                                                               {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}],
                                                              True,
                                                              [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                                               {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                                               {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                                               {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
                                                              ([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                                                                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                                                                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                                                                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}],
                                                               False,
                                                               [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                                                {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                                                {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                                                {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}])))
def test_sort_by_date(operation_list, sorter, expected):
    assert sort_by_date(operation_list, sorter) == expected


def test_sort_by_date_other_format(other_date_format, sorted_other_date_format):
    assert sort_by_date(other_date_format) == sorted_other_date_format


def test_sort_by_date_identical_date(identical_date_list, sorted_identical_date_list):
    assert sort_by_date(identical_date_list) == sorted_identical_date_list