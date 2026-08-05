"""
Функция get_mask_card_number принимает на вход номер карты и возвращает ее маску.
Номер карты замаскирован и отображается
в формате XXXX XX** **** XXXX, где X — это цифра номера. То есть,
 видны первые 6 цифр и последние 4 цифры,
остальные символы отображаются звездочками, номер разбит по блокам по 4 цифры, разделенным пробелами.

Пример работы функции:
7000792289606361     # входной аргумент
7000 79** **** 6361  # выход функции
Функция get_mask_account принимает на вход номер счета и возвращает его маску. Номер счета замаскирован и отображается
в формате
**XXXX, где X — это цифра номера. То есть видны только последние 4 цифры номера, а перед ними — две звездочки.

Пример работы функции:
73654108430135874305  # входной аргумент
**4305  # выход функции
"""


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    if len(list(card_number)) == 16 and card_number.isdigit() is True:
        return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:]}"
    else:
        return "Номер карты введен некорректно"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    if len(list(account_number)) == 20 and account_number.isdigit() is True:
        return f"**{account_number[-4:]}"
    else:
        return "Номер счета введен некорректно"


if __name__ == "__main__":
    card_number = str(input("Введите номер карты: "))
    account_number = str(input("Ведите номер счета: "))
    print(get_mask_card_number(card_number))
    print(get_mask_account(account_number))
