import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize('number, expected',
                         [
                             (1234567890123456, '1234 56** **** 3456'),
                             ('', 'Введен неверный номер карты/счета'),
                             (1234, 'Введен неверный номер карты/счета'),
                             (35383033474447895560, 'Введен неверный номер карты/счета')

                         ])
def test_get_mask_card_number(number, expected):
    assert get_mask_card_number(number) == expected


@pytest.mark.parametrize('number, expected',
                         [
                             (1234567890123456, 'Введен неверный номер карты/счета'),
                             (1234567890123457, 'Введен неверный номер карты/счета'),
                             (1234, 'Введен неверный номер карты/счета'),
                             (35383033474447895560, '**5560')
                         ])
def test_get_mask_account(number, expected):
    assert get_mask_account(number) == expected
