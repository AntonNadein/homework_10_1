import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("card_info, expected", [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("Visa Credit Cards 6831982476737658", "Visa Credit Cards 6831 98** **** 7658"),
    ("Счет 35383033474447895560", "Счет **5560"),
    ("Счет **1234", "Введен неверный номер карты/счета"),
    ("35383033474447895560", " **5560"),
], )
def test_mask_account_card(card_info, expected):
    assert mask_account_card(card_info) == expected


@pytest.mark.parametrize(
    "date_format, expected", [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2024-07-11", "11.07.2024")]
)
def test_get_date(date_format, expected):
    assert get_date(date_format) == expected
