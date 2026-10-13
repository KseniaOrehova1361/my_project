"""
Функция get_mask_card_number:
Тестирование правильности маскирования номера карты.
Проверка работы функции на различных входных форматах номеров карт, включая граничные случаи и нестандартные длины номеров.
Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты.

Функция get_mask_account:
Тестирование правильности маскирования номера счета.
Проверка работы функции с различными форматами и длинами номеров счетов.
Проверка, что функция корректно обрабатывает входные данные, где номер счета меньше ожидаемой длины
"""
import pytest

from src.masks import get_mask_card_number, get_mask_account



@pytest.mark.parametrize('card_number, expected', (('7000792289606361', '7000 79** **** 6361'),
                                                   ('4111111111111111', '4111 11** **** 1111'),
                                                   ('5105105105105100', '5105 10** **** 5100')))
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize('card_number', ((7000792289606361),
                                         (4111111111111.11)))
def test_get_mask_card_number_wrong_type(card_number):
    with pytest.raises(TypeError):
        get_mask_card_number(card_number)


@pytest.mark.parametrize('card_number', (('7000792289606'),
                                         ('41111111111111111111'),
                                         ('abcdefghigklmnop'),
                                         ('5467 8923 8548 0000')))
def test_get_mask_card_number_invalid_num(card_number):
    assert get_mask_card_number(card_number) == "Номер карты введен некорректно"


@pytest.mark.parametrize('account_number, expected', (('73654108430135874305', '**4305'),
                                                   ('34000000000000000000', '**0000'),
                                                   ('35674720123456789876', '**9876')))
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize('account_number', ((73654108430135874305),
                                         (3400000000000000.000)))
def test_get_mask_account_wrong_type(account_number):
    with pytest.raises(TypeError):
        get_mask_account(account_number)


@pytest.mark.parametrize('account_number', (('73654108430135'),
                                         ('41111111111111111111111'),
                                         ('abcdefghigklmnopqrst'),
                                         ('5467892356 8548000000')))
def test_get_account_invalid_num(account_number):
    assert get_mask_account(account_number) == "Номер счета введен некорректно"
