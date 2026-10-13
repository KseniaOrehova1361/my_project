"""
Функция mask_account_card:
Тесты для проверки, что функция корректно распознает и применяет нужный тип маскировки в зависимости от типа входных данных (карта или счет).
Параметризованные тесты с разными типами карт и счетов для проверки универсальности функции.
Тестирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам.

Функция get_date:
Тестирование правильности преобразования даты.
Проверка работы функции на различных входных форматах даты, включая граничные случаи и нестандартные строки с датами.
Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата.
"""


import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize('account_card, expected', (('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
                                                    ('Счет 64686473678894779589', 'Счет **9589'),
                                                    ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
                                                    ('Счет 73654108430135874305', 'Счет **4305'),
                                                   ('Visa Gold 5999414228426353', 'Visa Gold 5999 41** **** 6353')))

def test_mask_account_card(account_card, expected):
    assert mask_account_card(account_card) == expected


@pytest.mark.parametrize('account_card', (('Visa 7000792289606'),
                                         ('Счет 411111111111111111'),
                                         ('Счет 123456789'),
                                         ('Maestro 5467 8923 8548 0000')))
def test_mask_account_card_invalid_data(account_card):
    assert mask_account_card(account_card) == 'Данные введены некорректно'


@pytest.mark.parametrize('account_card', ((73654108430135874305),
                                         (683198247673765.8)))
def test_account_card_wrong_attribute(account_card):
    with pytest.raises(AttributeError):
        mask_account_card(account_card)


def test_get_date():
    assert get_date('2025-05-10T02:27:10.671407') == '10.05.2025'


@pytest.mark.parametrize('date', (('2025.05.18'),
                                  ('2006-09-03'),
                                  ('18.08.1998'),
                                  ('05-07-2020'),
                                  ('12/03/2013')))
def test_get_date_wrong_format(date):
    assert get_date(date) == "Неверный формат даты"


def test_get_date_no_date():
    assert get_date('') == "Неверный формат даты"

