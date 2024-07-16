import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_card_number_generator():
    card_generator = card_number_generator(1, 2)
    assert next(card_generator) == "0000 0000 0000 0001"
    assert next(card_generator) == "0000 0000 0000 0002"
    with pytest.raises(StopIteration):
        assert next(card_generator) == "0000 0000 0000 0003"


def test_card_number_generator_biggest_stop():
    card_generator = card_number_generator(1, 99999999999999999)
    assert next(card_generator) == "Заданы неверные стартовые значения"


def test_card_number_generator_revers():
    card_generator = card_number_generator(10, 1)
    assert next(card_generator) == "Заданы неверные стартовые значения"


def test_card_number_generator_negative_start():
    card_generator = card_number_generator(-50, 1)
    assert next(card_generator) == "Заданы неверные стартовые значения"


def test_transaction_descriptions(dict_transactions_generator):
    generation = transaction_descriptions(dict_transactions_generator)
    assert next(generation) == "Перевод организации"
    assert next(generation) == "Перевод со счета на счет"
    assert next(generation) == "Перевод со счета на счет"
    assert next(generation) == "Перевод с карты на карту"
    assert next(generation) == "Перевод организации"


def test_transaction_descriptions_null_dict():
    generation = transaction_descriptions([{}])
    assert next(generation) == "Нет ключа в словаре"


def test_transaction_descriptions_null_list():
    generation = transaction_descriptions([])
    assert next(generation) == "Передан пустой список"


def test_filter_by_currency(dict_transactions_generator):
    generation = filter_by_currency(dict_transactions_generator, "USD")
    generation1 = filter_by_currency(dict_transactions_generator, "RUB")
    assert next(generation) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generation) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(generation) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }
    assert next(generation1) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }


def test_filter_by_currency_null_list():
    generation = filter_by_currency([], "RUB")
    assert next(generation) == "Передан пустой список"


with pytest.raises(StopIteration):
    generation = filter_by_currency(
        [
            {
                "id": 873106923,
                "state": "EXECUTED",
                "date": "2019-03-23T01:09:46.296404",
                "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 44812258784861134719",
                "to": "Счет 74489636417521191160",
            }
        ],
        "UD",
    )
    next(generation)
