"""
В модуле widget создайте функцию mask_account_card, которая умеет обрабатывать информацию как о картах, так и о счетах.
Функция должна:
Принимать один аргумент — строку, содержащую тип и номер карты или счета.
Аргументом может быть строка типа:
Visa Platinum 7000792289606361, или Maestro 7000792289606361, или Счет 73654108430135874305.
Разделять строку на 2 аргумента (отдельно имя, отдельно номер) нельзя!

Возвращать строку с замаскированным номером. Для карт и счетов используйте разные типы маскировки.
Переиспользуйте уже существующие функции маскировки из вашего проекта, чтобы избежать дублирования кода.

Примеры входящих данных:
Maestro 1596837868705199
Счет 64686473678894779589
MasterCard 7158300734726758
Счет 35383033474447895560
Visa Classic 6831982476737658
Visa Platinum 8990922113665229
Visa Gold 5999414228426353
Счет 73654108430135874305

В том же модуле создайте функцию get_date, которая принимает на вход строку с датой в формате
"2025-05-10T02:27:10.671407" и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024").
"""

import datetime

from masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция принимает на вход имя и номер счета/карты и возвращает маску"""
    # разделяем строку на подстроки, отделяя номер счета/карты
    splited_account_card = account_card.split(" ")
    # запускаем цикл разделения на карты и счета
    if len(list(splited_account_card[-1])) == 16:
        # делаем маску номеру карты
        mask_card = get_mask_card_number(splited_account_card[-1])
        # заменяем номер карты в строке маской
        new_account_card = account_card.replace(splited_account_card[-1], mask_card)
    elif len(list(splited_account_card[-1])) == 20:
        # делаем маску номеру счета
        mask_account = get_mask_account(splited_account_card[-1])
        # заменяем номер счета в строке маской
        new_account_card = account_card.replace(splited_account_card[-1], mask_account)
    else:
        # отметаем случаи неверного ввода
        new_account_card = "Данные введены некорректно"
    return new_account_card


def get_date(iso_date: str) -> str:
    """Функция переводит дату из международного формата в формат 'ДД.ММ.ГГГГ'"""
    standard_format_date = datetime.datetime.strptime(iso_date, "%Y-%m-%dT%H:%M:%S.%f")
    return standard_format_date.strftime("%d.%m.%Y")


account_card = str(input("Ведите данные счета/карты: "))
print(mask_account_card(account_card))

iso_date = str(input("Введите дату: "))
print(get_date(iso_date))
