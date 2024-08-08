import pytest

from src.count_categories import count_operation


@pytest.mark.parametrize(
    "list_dict, expected",
    [
        (
            [
                {"description": "Перевод организации"},
                {"description": "Перевод с карты на карту"},
                {"description": "Перевод с карты на карту"},
                {"description": "Открытие вклада"},
                {"description": "Открытие вклада"},
                {"description": "Перевод с карты на карту"},
                {"description": "Перевод организации"},
                {"description": "Открытие вклада"},
                {"description": "Перевод организации"},
                {"description": "Перевод с карты на карту"},
                {"description": "Перевод организации"},
                {"description": "Перевод организации"},
                {"description": "Перевод со счета на счет"},
            ],
            {
                "Перевод организации": 5,
                "Перевод с карты на карту": 4,
                "Открытие вклада": 3,
                "Перевод со счета на счет": 1,
            },
        ),
        (
            [
                {"description": "Перевод организации"},
                {"description": "Перевод организации"},
                {"description": "Перевод с карты на карту"},
                {"description": "Открытие вклада"},
                {"description": "Перевод организации"},
                {"description": "Открытие вклада"},
                {"description": "Перевод с карты на карту"},
                {"description": ""},
                {"description": "Открытие вклада"},
                {"description": ""},
                {"description": ""},
                {"description": "Перевод организации"},
                {"description": ""},
            ],
            {
                "Перевод организации": 4,
                "Перевод с карты на карту": 2,
                "Открытие вклада": 3,
            },
        ),
    ],
)
def test_count_operation(list_dict, expected):
    result = count_operation(list_dict)
    assert result == expected


def test_count_operation_not_key():
    result = count_operation([{"descr": "Перевод организации"}])
    assert result == {}


def test_count_operation_category():
    result = count_operation(
        [
            {"description": "Перевод организации"},
            {"description": "Перевод организации"},
            {"description": "Перевод с карты на карту"},
            {"description": "Открытие вклада"},
        ],
        ["Перевод организации"],
    )
    assert result == {"Перевод организации": 2}
