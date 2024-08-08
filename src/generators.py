from typing import Any, Dict, Generator, List


def filter_by_currency(
    transactions: List[Dict[str, Any]], currency_code: str
) -> Generator[Any, None, None]:
    """Генератор возвращает транзакции, где валюта операции
    соответствует заданному коду (например, RUB)"""
    if transactions == []:
        yield "Передан пустой список"
    else:
        for i_dict in transactions:
            if currency_code in i_dict["operationAmount"]["currency"].get(
                "code"
            ):
                yield i_dict


def transaction_descriptions(
    transactions: List[Dict[str, Any]]
) -> Generator[str, None, None]:
    """Генератор принимает список словарей с транзакциями и
    возвращает описание каждой операции по очереди"""
    if transactions == []:
        yield "Передан пустой список"
    else:
        for i_dict in transactions:
            yield i_dict.get("description", "Нет ключа в словаре")


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    if start > stop or start < 0 or stop > 9999999999999999:
        yield "Заданы неверные стартовые значения"
    else:
        for number in range(start, stop + 1):
            number_str = f"{number:016}"
            formatted_number = (
                f"{number_str[:4]} {number_str[4:8]}"
                f" {number_str[8:12]} {number_str[12:]}"
            )
            yield formatted_number
