from unittest.mock import patch

import pytest

from src.utils import json_to_dict


@pytest.mark.parametrize(
    "name, exp",
    [
        ("operation.json", []),
        (".json", []),
        ("operation", []),
        ("", []),
    ],
)
def test_json_to_dict_bad_name(name, exp):
    test = json_to_dict(name)
    assert test == exp


@patch("json.load")
def test_json_to_dict(mock_json):
    test_file = [
        {
            "date": "2019-08-26T10:50:58.294041",
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "id": 441945886,
            "operationAmount": {
                "amount": "31957.58",
                "currency": {"code": "RUB", "name": "руб."},
            },
            "state": "EXECUTED",
            "to": "Счет 64686473678894779589",
        }
    ]
    mock_json.return_value = test_file
    assert json_to_dict("operations.json") == [
        {
            "date": "2019-08-26T10:50:58.294041",
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "id": 441945886,
            "operationAmount": {
                "amount": "31957.58",
                "currency": {"code": "RUB", "name": "руб."},
            },
            "state": "EXECUTED",
            "to": "Счет 64686473678894779589",
        }
    ]
