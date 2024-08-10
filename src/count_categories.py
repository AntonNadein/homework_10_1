from typing import Any, Dict, List

from pyflakes.checker import counter


def count_operation(
    list_dict: List[Dict[str, Any]],
    list_category: List[str] = [
        "Перевод организации",
        "Перевод с карты на карту",
        "Открытие вклада",
        "Перевод со счета на счет",
    ],
) -> Dict[str, int]:
    """Функция подсчета категорий банковских операций"""
    list_1 = []
    for i in list_dict:
        if i.get("description") in list_category:
            list_1.append(i.get("description"))
    counted = counter(list_1)
    return counted
